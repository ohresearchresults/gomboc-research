/* Standalone public-catalog explorer. No runtime state or private application code. */
"use strict";

(() => {
  const $ = (id) => document.getElementById(id);
  const GITHUB = "https://github.com/ohresearchresults/gomboc-research/blob/main/";
  const STUDIES = { figure: "Figure", minimum: "Minimum" };
  const MIN_SCALE = 0.04;
  const CARD = { width: 292, height: 116, column: 400, row: 150 };
  const state = { study: "figure", root: null, selected: null, expanded: new Set(), visible: [], positions: new Map(), width: 0, height: 0, x: 0, y: 0, scale: 1 };
  let data, branches, reports, children;

  function element(tag, className, text) {
    const el = document.createElement(tag);
    if (className) el.className = className;
    if (text !== undefined) el.textContent = text;
    return el;
  }
  function link(text, path, className = "") {
    const el = element("a", className, text);
    el.href = GITHUB + path.split("/").map(encodeURIComponent).join("/");
    return el;
  }
  function number(id) { return id.split("-").at(-1); }
  function statusText(branch) { return `${branch.recorded_status === "open" ? "Open" : "Closed"} at saved checkpoint`; }
  function roots(study) { return data.branches.filter((branch) => branch.study === study && branch.parent === null); }
  function ancestry(id) {
    const path = [];
    for (let branch = branches.get(id); branch; branch = branches.get(branch.parent)) path.unshift(branch.id);
    return path;
  }
  function announce(text) { $("announcer").textContent = text; }
  function updateAddress() {
    // HTTP deep links can be copied and opened directly; local-file rendering also works.
    if (location.protocol === "http:" || location.protocol === "https:") history.replaceState(null, "", `${location.pathname}${location.search}#${state.selected || state.study}`);
  }

  function initialExpansion(root) {
    state.expanded = new Set();
    function expand(id) {
      state.expanded.add(id);
      for (const child of children.get(id)) expand(child);
    }
    for (const branch of root ? [branches.get(root)] : roots(state.study)) expand(branch.id);
  }
  function updateStudyControls() {
    for (const button of document.querySelectorAll("[data-study]")) {
      const current = button.dataset.study === state.study;
      button.setAttribute("aria-selected", String(current));
      button.tabIndex = current ? 0 : -1;
    }
    $("study-panel").setAttribute("aria-labelledby", `tab-${state.study}`);
    const all = element("option", "", "All branches");
    all.value = "";
    $("root-select").replaceChildren(all, ...roots(state.study).map((branch) => {
      const option = element("option", "", `${number(branch.id)} · ${branch.title}`);
      option.value = branch.id;
      return option;
    }));
    $("root-select").value = state.root || "";
    $("root-select").title = state.root ? branches.get(state.root).title : "All recorded branches in this study";
  }
  function chooseStudy(study) {
    state.study = study;
    state.root = null;
    state.selected = null;
    initialExpansion(null);
    closeSearch();
    updateStudyControls();
    setInspectorOpen(false);
    $("inspector-content").replaceChildren();
    renderMap();
    updateAddress();
    announce(`${STUDIES[study]}: all ${state.visible.length} branches shown.`);
  }
  function chooseRoot(id) {
    if (!id) return chooseStudy(state.study);
    const branch = branches.get(id);
    state.study = branch.study;
    state.root = id;
    state.selected = id;
    initialExpansion(id);
    closeSearch();
    updateStudyControls();
    renderMap();
    renderInspector();
    setInspectorOpen(false);
    updateAddress();
    announce(`${STUDIES[state.study]}: ${branch.title}. ${state.visible.length} branches shown.`);
  }
  function navigateTo(id, focus = false) {
    if (!branches.has(id)) return;
    const path = ancestry(id);
    const study = branches.get(id).study;
    const changedStudy = state.study !== study;
    state.study = study;
    if (changedStudy) state.root = null;
    if (state.root && state.root !== path[0]) {
      state.root = path[0];
      initialExpansion(state.root);
    }
    if (changedStudy || !state.expanded.size) initialExpansion(state.root);
    for (const ancestor of path.slice(0, -1)) state.expanded.add(ancestor);
    state.selected = id;
    closeSearch();
    updateStudyControls();
    renderMap();
    renderInspector();
    setInspectorOpen(true);
    focusSelection();
    updateAddress();
    if (focus) document.querySelector(`[data-node-id="${id}"] .node-card`).focus({ preventScroll: true });
    announce(`${branches.get(id).title}. ${statusText(branches.get(id))}.`);
  }
  function selectCard(id) {
    state.selected = id;
    highlightSelection();
    renderInspector();
    setInspectorOpen(true);
    focusSelection();
    updateAddress();
    announce(`${branches.get(id).title}. ${statusText(branches.get(id))}. Details updated.`);
  }

  function layout() {
    state.visible = [];
    state.positions = new Map();
    // Each component contains only its recorded parent edges. Pack the separate
    // trees into available rows without inventing a common scientific ancestor.
    const trees = (state.root ? [branches.get(state.root)] : roots(state.study)).map((root) => {
      const columns = [];
      function visit(id, depth) {
        state.visible.push(id);
        (columns[depth] ||= []).push(id);
        if (state.expanded.has(id)) for (const child of children.get(id)) visit(child, depth + 1);
      }
      visit(root.id, 0);
      const rows = Math.max(...columns.map((column) => column.length));
      const height = (rows - 1) * CARD.row + CARD.height;
      const width = (columns.length - 1) * CARD.column + CARD.width;
      return { columns, rows, width, height };
    });
    const maxWidth = Math.max(...trees.map((tree) => tree.width));
    const gap = CARD.row;
    const shelves = [];
    state.width = 0;
    state.height = 0;
    for (const tree of trees) {
      let shelf = shelves.find((row) => tree.height <= row.height && row.used + gap + tree.width <= maxWidth);
      if (!shelf) {
        shelf = { y: shelves.length ? state.height + gap : 0, height: tree.height, used: 0 };
        shelves.push(shelf);
        state.height = shelf.y + tree.height;
      }
      const left = shelf.used ? shelf.used + gap : 0;
      tree.columns.forEach((column, depth) => {
        const top = shelf.y + (tree.rows - column.length) * CARD.row / 2;
        column.forEach((id, row) => state.positions.set(id, { x: left + depth * CARD.column, y: top + row * CARD.row }));
      });
      shelf.used = left + tree.width;
      state.width = Math.max(state.width, shelf.used);
    }
  }
  function renderMap() {
    layout();
    const fragment = document.createDocumentFragment();
    const edges = document.createDocumentFragment();
    for (const id of state.visible) {
      const branch = branches.get(id);
      const point = state.positions.get(id);
      const node = element("div", "node");
      node.dataset.nodeId = id;
      node.style.left = `${point.x}px`;
      node.style.top = `${point.y}px`;
      const card = element("button", "node-card");
      card.type = "button";
      card.title = branch.title;
      card.setAttribute("aria-label", `${STUDIES[branch.study]} branch ${number(id)}. ${branch.title}. ${statusText(branch)}. ${branch.reports.length} linked reports. Select to inspect.`);
      card.setAttribute("aria-controls", "inspector-content");
      card.append(element("span", "node-title", branch.title));
      card.addEventListener("click", () => selectCard(id));
      card.addEventListener("focus", () => ensureVisible(id));
      node.append(card);
      const childCount = children.get(id).length;
      if (childCount) {
        const expanded = state.expanded.has(id);
        const toggle = element("button", "expand-node", expanded ? "−" : "+");
        toggle.type = "button";
        toggle.title = `${expanded ? "Collapse" : "Expand"} ${childCount} child ${childCount === 1 ? "branch" : "branches"}`;
        toggle.setAttribute("aria-label", `${toggle.title} of ${branch.title}`);
        toggle.setAttribute("aria-expanded", String(expanded));
        toggle.addEventListener("click", () => {
          if (state.expanded.has(id)) {
            state.expanded.delete(id);
            if (ancestry(state.selected).includes(id)) state.selected = id;
          } else state.expanded.add(id);
          renderMap();
          renderInspector();
          updateAddress();
          document.querySelector(`[data-node-id="${id}"] .expand-node`).focus({ preventScroll: true });
          announce(`${state.visible.length} branches shown. ${branches.get(id).title} ${state.expanded.has(id) ? "expanded" : "collapsed"}.`);
        });
        toggle.addEventListener("focus", () => ensureVisible(id));
        node.append(toggle);
      }
      fragment.append(node);
      if (branch.parent && state.positions.has(branch.parent)) {
        const parent = state.positions.get(branch.parent);
        const x1 = parent.x + CARD.width;
        const y1 = parent.y + CARD.height / 2;
        const x2 = point.x;
        const y2 = point.y + CARD.height / 2;
        const middle = (x1 + x2) / 2;
        const edge = document.createElementNS("http://www.w3.org/2000/svg", "path");
        edge.setAttribute("d", `M${x1},${y1} C${middle},${y1} ${middle},${y2} ${x2},${y2}`);
        edge.setAttribute("class", "branch-edge");
        edge.dataset.child = id;
        edges.append(edge);
      }
    }
    $("map-nodes").replaceChildren(fragment);
    $("map-edges").replaceChildren(edges);
    $("map-edges").setAttribute("width", String(state.width));
    $("map-edges").setAttribute("height", String(state.height));
    $("map-world").style.width = `${state.width}px`;
    $("map-world").style.height = `${state.height}px`;
    highlightSelection();
    fitView();
  }
  function highlightSelection() {
    const lineage = new Set(ancestry(state.selected));
    for (const node of document.querySelectorAll("[data-node-id]")) {
      const selected = node.dataset.nodeId === state.selected;
      node.classList.toggle("selected", selected);
      node.classList.toggle("ancestor", !selected && lineage.has(node.dataset.nodeId));
      node.querySelector(".node-card").setAttribute("aria-pressed", String(selected));
      node.querySelector(".node-card").setAttribute("aria-expanded", String(selected && !$("inspector").hidden));
    }
    for (const edge of document.querySelectorAll(".branch-edge")) edge.classList.toggle("lineage", lineage.has(edge.dataset.child));
  }

  function setInspectorOpen(open) {
    $("inspector").hidden = !open;
    $("study-panel").classList.toggle("has-inspector", open);
    for (const card of document.querySelectorAll(".node-card")) {
      card.setAttribute("aria-expanded", String(open && card.closest("[data-node-id]").dataset.nodeId === state.selected));
    }
  }
  function closeInspector() {
    setInspectorOpen(false);
    document.querySelector(`[data-node-id="${state.selected}"] .node-card`)?.focus({ preventScroll: true });
  }
  function relatedButton(id) {
    const branch = branches.get(id);
    const button = element("button", "related-branch");
    button.append(element("span", "relation-number", `#${number(id)} ↗`), document.createTextNode(branch.title));
    button.addEventListener("click", () => navigateTo(id, true));
    return button;
  }
  function section(title, count) {
    const el = element("section", "inspector-section");
    const heading = element("h3", "section-title", title);
    if (count !== undefined) heading.append(element("span", "", String(count)));
    el.append(heading);
    return el;
  }
  function reportItem(report) {
    const item = element("li");
    const a = link("", report.path);
    a.setAttribute("aria-label", `${report.title}. ${report.id}, ${report.date}. Historical AI scientific report on GitHub.`);
    const meta = element("span", "report-meta");
    meta.append(element("span", "", report.id), element("time", "", report.date));
    meta.lastChild.dateTime = report.date;
    a.append(meta, element("span", "report-title", report.title), element("span", "report-arrow", " ↗"));
    item.append(a);
    return item;
  }
  function renderInspector() {
    if (!state.selected) return;
    const branch = branches.get(state.selected);
    const content = $("inspector-content");
    const status = element("div", `detail-status ${branch.recorded_status}`);
    status.append(element("i", `status-mark ${branch.recorded_status}`), document.createTextNode(statusText(branch)));
    content.replaceChildren(element("p", "detail-id", branch.id), element("h2", "detail-title", branch.title), status);
    content.append(element("p", "evidence-note", "Archived AI work. Branch status does not verify its claims."));
    if (branch.unavailable_report_count) content.append(element("p", "unavailable-note", `${branch.unavailable_report_count} additional report reference is unavailable. Its identifier and reason are not retained in the public index.`));
    const parent = section("Recorded parent");
    if (branch.parent) parent.append(relatedButton(branch.parent));
    else {
      const note = element("p", "parent-empty", "No parent recorded");
      note.append(element("span", "", `One of ${data.stats.studies[branch.study].roots} root directions in ${STUDIES[branch.study]}.`));
      parent.append(note);
    }
    const descendants = section("Child branches", children.get(branch.id).length);
    if (children.get(branch.id).length) descendants.append(...children.get(branch.id).map(relatedButton));
    else descendants.append(element("p", "empty-reports", "No child branches recorded."));
    const evidence = section("Linked reports", branch.reports.length);
    evidence.append(element("p", "evidence-note", "Historical AI scientific reports · open on GitHub"));
    if (!branch.reports.length) evidence.append(element("p", "empty-reports", "No linked public report in this index. Other evidence, such as materials, is outside this map."));
    else {
      const list = element("ol", "report-list");
      list.id = "selected-reports";
      // Keep the catalog order; report dates do not establish scientific ancestry.
      list.append(...branch.reports.slice(0, 5).map((id) => reportItem(reports.get(id))));
      evidence.append(list);
      if (branch.reports.length > 5) {
        const show = element("button", "show-reports", `Show all ${branch.reports.length} reports ↓`);
        show.setAttribute("aria-expanded", "false");
        show.setAttribute("aria-controls", list.id);
        show.addEventListener("click", () => {
          const expanded = show.getAttribute("aria-expanded") === "true";
          list.replaceChildren(...branch.reports.slice(0, expanded ? 5 : undefined).map((id) => reportItem(reports.get(id))));
          show.setAttribute("aria-expanded", String(!expanded));
          show.textContent = expanded ? `Show all ${branch.reports.length} reports ↓` : "Show fewer reports ↑";
          announce(`${expanded ? 5 : branch.reports.length} reports displayed.`);
        });
        evidence.append(show);
      }
    }
    content.append(parent, descendants, evidence, link("Open the complete branch index ↗", "catalog/branches.md", "open-index"));
    $("inspector").scrollTop = 0;
  }

  function applyTransform() {
    $("map-world").style.transform = `translate(${state.x}px,${state.y}px) scale(${state.scale})`;
    $("zoom-level").textContent = `${Math.round(state.scale * 100)}%`;
    $("zoom-out").disabled = state.scale <= MIN_SCALE;
    $("zoom-in").disabled = state.scale >= 1.8;
  }
  function fitView() {
    const viewport = $("map-viewport");
    const width = viewport.clientWidth;
    const height = viewport.clientHeight;
    if (!width || !height || !state.width) return;
    const top = 40, bottom = 68;
    state.scale = Math.max(MIN_SCALE, Math.min(1, (width - 48) / state.width, (height - top - bottom) / state.height));
    state.x = (width - state.width * state.scale) / 2;
    state.y = top + (height - top - bottom - state.height * state.scale) / 2;
    applyTransform();
  }
  function focusSelection() {
    const point = state.positions.get(state.selected);
    if (!point) return;
    const viewport = $("map-viewport");
    state.scale = Math.max(state.scale, Math.min(0.85, (viewport.clientWidth - 48) / CARD.width));
    state.x = viewport.clientWidth / 2 - (point.x + CARD.width / 2) * state.scale;
    state.y = viewport.clientHeight / 2 - (point.y + CARD.height / 2) * state.scale;
    applyTransform();
  }
  function zoom(factor, origin) {
    const viewport = $("map-viewport");
    const anchor = origin || { x: viewport.clientWidth / 2, y: viewport.clientHeight / 2 };
    const scale = Math.max(MIN_SCALE, Math.min(1.8, state.scale * factor));
    state.x = anchor.x - (anchor.x - state.x) * scale / state.scale;
    state.y = anchor.y - (anchor.y - state.y) * scale / state.scale;
    state.scale = scale;
    applyTransform();
  }
  function ensureVisible(id) {
    const point = state.positions.get(id);
    if (!point) return;
    const viewport = $("map-viewport");
    const left = state.x + point.x * state.scale;
    const top = state.y + point.y * state.scale;
    const right = left + CARD.width * state.scale;
    const bottom = top + CARD.height * state.scale;
    if (left < 12) state.x += 12 - left;
    else if (right > viewport.clientWidth - 12) state.x -= right - viewport.clientWidth + 12;
    if (top < 44) state.y += 44 - top;
    else if (bottom > viewport.clientHeight - 74) state.y -= bottom - viewport.clientHeight + 74;
    applyTransform();
  }

  function closeSearch() {
    $("search-results").hidden = true;
    $("branch-search").setAttribute("aria-expanded", "false");
  }
  function normalize(text) { return text.normalize("NFKD").replace(/[\u0300-\u036f]/g, "").toLowerCase(); }
  function search() {
    const query = normalize($("branch-search").value.trim());
    if (!query) return closeSearch();
    const words = query.split(/\s+/);
    const matches = data.branches.filter((branch) => {
      const text = normalize(`${branch.title} ${branch.id} ${branch.study} ${branch.reports.join(" ")}`);
      return words.every((word) => text.includes(word));
    });
    const panel = $("search-results");
    panel.replaceChildren(element("p", "results-heading", `${matches.length} ${matches.length === 1 ? "branch" : "branches"} across both studies`));
    for (const branch of matches) {
      const result = element("button", "search-result");
      result.append(element("span", "", branch.id), element("strong", "", branch.title));
      result.addEventListener("click", () => navigateTo(branch.id, true));
      panel.append(result);
    }
    if (!matches.length) panel.append(element("p", "search-empty", "No matching branches. Try a shorter phrase, branch ID, or linked report ID."));
    panel.hidden = false;
    $("branch-search").setAttribute("aria-expanded", "true");
    announce(`${matches.length} matching branches across both studies.`);
  }

  function bindControls() {
    $("root-select").addEventListener("change", (event) => chooseRoot(event.target.value));
    const tabs = [...document.querySelectorAll("[data-study]")];
    for (const button of tabs) {
      button.addEventListener("click", () => chooseStudy(button.dataset.study));
      button.addEventListener("keydown", (event) => {
        if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
        event.preventDefault();
        const tab = event.key === "Home" ? tabs[0] : event.key === "End" ? tabs[1] : tabs.find((item) => item !== button);
        tab.click();
        tab.focus();
      });
    }
    $("inspector-close").addEventListener("click", closeInspector);
    $("reset-view").addEventListener("click", () => chooseRoot(state.root));
    $("fit-view").addEventListener("click", fitView);
    $("zoom-in").addEventListener("click", () => zoom(1.2));
    $("zoom-out").addEventListener("click", () => zoom(1 / 1.2));
    $("branch-search").addEventListener("input", search);
    $("branch-search").addEventListener("focus", search);
    $("branch-search").addEventListener("keydown", (event) => {
      if (event.key === "ArrowDown" && !$("search-results").hidden) {
        event.preventDefault();
        $("search-results").querySelector("button")?.focus();
      }
      if (event.key === "Escape") closeSearch();
    });
    $("search-results").addEventListener("keydown", (event) => {
      const buttons = [...$("search-results").querySelectorAll("button")];
      const index = buttons.indexOf(document.activeElement);
      if (event.key === "ArrowDown" || event.key === "ArrowUp") {
        event.preventDefault();
        const next = index + (event.key === "ArrowDown" ? 1 : -1);
        if (next < 0) $("branch-search").focus();
        else buttons[Math.min(next, buttons.length - 1)]?.focus();
      }
      if (event.key === "Escape") { $("branch-search").focus(); closeSearch(); }
    });
    document.addEventListener("pointerdown", (event) => { if (!event.target.closest(".search-area")) closeSearch(); });
    document.addEventListener("focusin", (event) => { if (!event.target.closest(".search-area")) closeSearch(); });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !event.target.closest("input,select,dialog") && !$("inspector").hidden) closeInspector();
      if (event.key === "/" && !event.target.closest("input,select,textarea,dialog")) {
        event.preventDefault();
        $("branch-search").focus();
      }
    });
    const viewport = $("map-viewport");
    let drag;
    viewport.addEventListener("pointerdown", (event) => {
      if (event.button !== 0 || event.target.closest("button")) return;
      drag = { id: event.pointerId, x: event.clientX, y: event.clientY, originX: state.x, originY: state.y };
      viewport.setPointerCapture(event.pointerId);
      viewport.classList.add("dragging");
      viewport.focus({ preventScroll: true });
    });
    viewport.addEventListener("pointermove", (event) => {
      if (!drag || drag.id !== event.pointerId) return;
      state.x = drag.originX + event.clientX - drag.x;
      state.y = drag.originY + event.clientY - drag.y;
      applyTransform();
    });
    function endDrag(event) {
      if (!drag || event.pointerId !== drag.id) return;
      if (viewport.hasPointerCapture(event.pointerId)) viewport.releasePointerCapture(event.pointerId);
      drag = null;
      viewport.classList.remove("dragging");
    }
    viewport.addEventListener("pointerup", endDrag);
    viewport.addEventListener("pointercancel", endDrag);
    viewport.addEventListener("lostpointercapture", endDrag);
    viewport.addEventListener("wheel", (event) => {
      event.preventDefault();
      const unit = event.deltaMode === 1 ? 16 : event.deltaMode === 2 ? viewport.clientHeight : 1;
      if (event.ctrlKey || event.metaKey) {
        const rect = viewport.getBoundingClientRect();
        zoom(Math.exp(-event.deltaY * unit * 0.006), { x: event.clientX - rect.left, y: event.clientY - rect.top });
      } else {
        state.x -= (event.shiftKey ? event.deltaY : event.deltaX) * unit;
        state.y -= event.shiftKey ? 0 : event.deltaY * unit;
        applyTransform();
      }
    }, { passive: false });
    viewport.addEventListener("keydown", (event) => {
      if (event.target !== viewport) return;
      const key = event.key.toLowerCase();
      const offsets = { arrowleft: [55, 0], arrowright: [-55, 0], arrowup: [0, 55], arrowdown: [0, -55] };
      if (offsets[key]) {
        event.preventDefault();
        state.x += offsets[key][0]; state.y += offsets[key][1]; applyTransform();
      } else if (["+", "=", "-", "f", "home"].includes(key)) {
        event.preventDefault();
        if (key === "f" || key === "home") fitView();
        else zoom(key === "-" ? 1 / 1.2 : 1.2);
      }
    });
    new ResizeObserver(() => $("inspector").hidden ? fitView() : focusSelection()).observe(viewport);
    $("coverage-open").addEventListener("click", (event) => {
      event.preventDefault();
      $("coverage-dialog").showModal();
    });
    $("coverage-close").addEventListener("click", () => $("coverage-dialog").close());
    window.addEventListener("hashchange", () => {
      const id = location.hash.slice(1);
      if (STUDIES[id]) chooseStudy(id);
      else if (branches.has(id) && state.selected !== id) navigateTo(id);
    });
  }

  function initialize() {
    data = JSON.parse($("research-data").textContent);
    if (data.schema_version !== 1 || !data.branches?.length || !data.reports?.length) throw new Error("Missing or unsupported public map data. Run the map builder.");
    branches = new Map(data.branches.map((branch) => [branch.id, branch]));
    reports = new Map(data.reports.map((report) => [report.id, report]));
    children = new Map(data.branches.map((branch) => [branch.id, []]));
    for (const branch of data.branches) {
      if (branch.parent !== null) {
        if (!branches.has(branch.parent) || branches.get(branch.parent).study !== branch.study) throw new Error(`Invalid recorded parent for ${branch.id}`);
        children.get(branch.parent).push(branch.id);
      }
      const seen = new Set([branch.id]);
      for (let parent = branch.parent; parent !== null; parent = branches.get(parent)?.parent ?? null) {
        if (seen.has(parent)) throw new Error("Cycle in recorded branch parents");
        seen.add(parent);
      }
      if (branch.reports.some((id) => !reports.has(id))) throw new Error(`Missing report metadata for ${branch.id}`);
    }
    if (branches.size !== data.branches.length || reports.size !== data.reports.length) throw new Error("Duplicate catalog identifiers");
    const coverage = $("coverage-detail");
    coverage.append(element("p", "", `${data.stats.branches} branches contain ${data.stats.report_links.toLocaleString("en-US")} report links to ${data.stats.linked_reports} unique reports. Reports can be shared by branches. ${data.stats.unlinked_reports.length} of the ${data.stats.reports} indexed reports have no recorded branch link:`));
    for (const id of data.stats.unlinked_reports) {
      const report = reports.get(id);
      coverage.append(link(`${id} · ${report.title} ↗`, report.path, "unlinked-report"));
    }
    const unavailable = data.branches.filter((branch) => branch.unavailable_report_count);
    const note = element("p", "", `${data.stats.unavailable_reports} additional report reference is unavailable in the branch index. `);
    for (const branch of unavailable) {
      const button = element("button", "show-reports", `Inspect ${branch.id} →`);
      button.addEventListener("click", () => { $("coverage-dialog").close(); navigateTo(branch.id, true); });
      note.append(button);
    }
    coverage.append(note);
    bindControls();
    const params = new URLSearchParams(location.search);
    const selected = location.hash.slice(1) || params.get("branch");
    const study = STUDIES[selected] ? selected : params.get("study");
    if (selected && branches.has(selected)) navigateTo(selected);
    else chooseStudy(study && STUDIES[study] ? study : "figure");
    document.documentElement.dataset.mapReady = "true";
  }

  try { initialize(); }
  catch (error) {
    console.error("Research map initialization failed:", error);
    const message = element("div", "fatal-message", `The research map could not load: ${error.message} `);
    message.setAttribute("role", "alert");
    message.append(link("Read the static branch catalog ↗", "catalog/branches.md"));
    document.body.append(message);
    document.documentElement.dataset.mapReady = "error";
  }
})();
