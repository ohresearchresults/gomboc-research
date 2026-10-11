# minimum-0005

Historical AI scientific report · saved 2026-09-07 UTC. Claims below retain their original status and have not all been independently checked. The current retained construction is C622; the C<500 search remains open.

Public text derivative: internal-record-identifiers-replaced.

---

# KIAS polyhedral Gömböc lead: speaker identified; construction evidence remains unresolved

**Determination as of 7 September 2026:** The KIAS lead is now attributable to **Tancredi Schettini-Gherardini, University of Bonn**. His listed talk is **“Knot-able polyhedric progress in the path to AI-assisted discovery.”** The institutional program connects that talk to the construction of a polyhedral Gömböc. However, I did not recover its defining geometry, mass convention, reference centre, equilibrium certificate, feature counts, corresponding manuscript, or any minimum claim. Consequently, this investigation establishes a named external announcement but supplies **no new verified upper bound, lower bound, or priority determination**. [KIAS program](https://symposia.kias.re.kr/AI-Math2026/page/ai-math-act-2026)

## 1. Parent and current mathematical baseline

This continues immutable parent `minimum-0002`, recorded SHA-256 `e7d6c4debb811f99e29cea6957479b8dba1b3f8a8eb8e20689ec28fd5e654103`. I read its literal payload and the newer coordinator entry. The parent’s unidentified-speaker limitation is superseded below. Its earlier internal lower bound of 24 is also superseded, independently of this investigation: the current journal accepts Clear Atlas13’s seven-point reflection theorem, giving `V≥8`, `F≥8`, and hence **`28≤C_min≤1374`**. This is the supplied research baseline, not a newly established published theorem or an audit performed in this assignment. The journal does not assert attainment at 28. :contentReference[oaicite:0]{index=0} :contentReference[oaicite:1]{index=1}

The accepted upper witness remains `FUSION258_PN03_C1374`, with `(V,E,F)=(258,687,431)` and strict own-volume-centroid `(S,U,H)=(1,1,0)`. No new object was reconstructed here, and no external object is being substituted for that inherited witness. :contentReference[oaicite:2]{index=2}

## 2. What the KIAS source actually establishes

The speaker identification is supported by indexed passages of the **official KIAS page**, rather than inferred from a similar research topic. One passage joins the speaker’s name and Bonn affiliation to the exact title; another joins the same entry to the phrase **“the construction of a polyhedral Gömböc.”** The abstract’s other subjects are folded statistics for symmetric Dyck paths and Harer–Zagier factorisability for three- and four-strand knots. It presents the three subjects as AI-assisted results, while distinguishing how AI was used in each. [KIAS program](https://symposia.kias.re.kr/AI-Math2026/page/ai-math-act-2026)

The ACT page gives **2–8 August 2026** for that thematic week. Participant Minho Song’s independent personal report gives **3–7 August 2026** for its working week. I did not recover the specific day or time of this talk, evidence that it was delivered exactly as advertised, or the program entry’s original posting/revision date. The event dates must not be presented as a verified manuscript-publication date. [KIAS program](https://symposia.kias.re.kr/AI-Math2026/page/ai-math-act-2026); [Minho Song’s program report](https://minhosong.github.io/ai-math.html)

### Retrieval limitation and recovery route

Direct retrieval of the KIAS ACT page repeatedly produced an empty parsed body, although search indexing returned meaningful passages. Direct retrieval of the main program and related program routes did not expose the missing technical material either; an attempted container download also failed. These failures are not evidence that the page lacks attachments or that no recording exists.

The productive retrieval step was to search the unusual title and then inspect the adjacent indexed speaker entry. For continuation, the exact title printed above and the following query are sufficient to recover the named institutional lead:

`site:symposia.kias.re.kr/AI-Math2026 "Schettini-Gherardini"`

This is a recovery route for an announcement, **not a reconstruction recipe for a polyhedron**. I did not obtain a full HTML snapshot suitable for establishing all page contents or a historical posting date.

## 3. Independent identification of the speaker

The speaker’s own website uses the spelling **Tancredi Schettini Gherardini**, without the surname hyphen used by KIAS. It identifies him as a Bonn postdoctoral researcher working on computation and AI for mathematical discovery. Thus the personal site is an independently supported continuation target, not a guessed association based on the name alone. [Author homepage](https://tancredi-schettini-gherardini.github.io/)

The public GitHub account is **`Tancredi-Schettini-Gherardini`**. The institutional Bonn workshop described below also independently lists the same researcher among its organizers. [Author GitHub](https://github.com/Tancredi-Schettini-Gherardini); [Bonn event record](https://math-events.uni-bonn.de/event/1088/)

**Speaker identity does not establish the construction’s complete author list.** I recovered no Gömböc-specific coauthor statement. His other collaborators and project leaders must not be assigned authorship of this construction by association.

## 4. Following the speaker’s papers, code, and subsequent institutional program

### Personal publication and talk lists

I inspected the author’s publication and talk pages. Neither exposed a Gömböc manuscript, coordinate supplement, certificate, slides for the KIAS talk, or a link to its recording. The publication page’s latest displayed work is the February 2026 Nirenberg-problem paper, while arXiv contains later work; consequently, that personal list is demonstrably not a complete account of his 2026 output. Its silence is only a limited negative finding. [Publications](https://tancredi-schettini-gherardini.github.io/papers.html); [Talks](https://tancredi-schettini-gherardini.github.io/talks.html)

### Direct arXiv author search

The direct all-archive author query `Gherardini, T S` returned **12 entries**, all of whose displayed titles and abstracts were inspected. No entry in that result set announced the polyhedral construction or the Dyck-path project. This is a bounded statement about the returned author search, not a claim that no manuscript exists under another indexing form, with other authors, or outside arXiv. [Exact all-archive query](https://arxiv.org/search/?query=Gherardini%2C+T+S&searchtype=author)

Two recent papers are especially important to distinguish from the target:

- **arXiv:2605.26234**, *Minimal surfaces, Knots, and Neural Networks*, with Marco Usula: v1 **25 May 2026**, v2 **9 June 2026**. Its problem is near-minimal surfaces in hyperbolic four-space meeting prescribed knots at infinity—not equilibria of a homogeneous three-dimensional polyhedral solid. [Paper record](https://arxiv.org/abs/2605.26234)
- **arXiv:2607.28733**, *A user’s guide to PINNs in geometric analysis: lessons from the asymptotic Plateau problem*: v1 **30 July 2026**. It is a methodological companion to that minimal-surface project, not a Gömböc construction paper. [Paper record](https://arxiv.org/abs/2607.28733)

These records were examined to resolve attribution and scope. I did not treat their numerical methods or their unrelated geometries as evidence for the KIAS polyhedron.

### Public code repositories

The GitHub repositories tab displayed two public repositories: **`deep_plateau`**, explicitly associated with arXiv:2605.26234v2, and **`P5CY4ML`**, associated with arXiv:2311.17146. Neither displayed description supplies a Gömböc reconstruction. The page also reported loading errors in ancillary components, so the defensible conclusion is that no such repository was recovered from the inspected account listing—not that the author has no other accessible code anywhere. [Repositories tab](https://github.com/Tancredi-Schettini-Gherardini?tab=repositories)

### The subsequent Bonn workshop was followed, not merely proposed as a lead

The author’s seminar page led to the workshop **Actions and Intuition: Algebra via AI**, **31 August–4 September 2026**. I followed the official Bonn event record to the linked MPIM-hosted program, headed *Actions and Intuition: Representation Theory via AI*. Both identify him as an organizer. [Bonn event record](https://math-events.uni-bonn.de/event/1088/); [MPIM-hosted program](https://nehme.docs.mpim-bonn.mpg.de/ai-for-mathematical-discovery/)

The program includes talks, project sessions, and named working groups concerning algebraic/combinatorial topics. Its inspected contents provide no Gömböc project entry, coordinate file, proof, or link to the KIAS talk. Therefore this route does **not** presently resolve the construction. A generic instruction to search that workshop again would repeat work already performed.

### Recordings and broader searches

Searches for the exact KIAS title and the speaker’s name with KIAS/video terms did not identify the target recording. They did locate unrelated presentations on exotic spheres and minimal surfaces. Those are not substitutes for the announced polyhedral result. Searches combining the speaker’s name, Gömböc spelling variants, and polyhedral/monostatic terminology, including institutional and repository-focused searches, produced no additional construction document that could be attributed and inspected.

No external author or organizer was contacted.

## 5. A useful independent corroboration of the abstract’s knot component

A separate, identifiable publication confirms that this researcher was involved in a concrete issue closely matching the knot component of the KIAS abstract:

**Andreani Petrou and Shinobu Hikami**, *A relation between the HOMFLY-PT and Kauffman polynomials via characters*, **JHEP 09 (2026) 027**, DOI **10.1007/JHEP09(2026)027**. The publisher records **received 20 April 2026**, **accepted 9 July 2026**, and **published/version of record 2 September 2026**. Its acknowledgment credits **Tancredi Schettini Gherardini** with identifying a miscalculation in a purported four-strand counterexample that an earlier preprint version had incorrectly claimed. I inspected the publisher’s acknowledgment and publication metadata directly. [Publisher article and acknowledgment](https://link.springer.com/article/10.1007/JHEP09%282026%29027)

This corroborates a substantive connection between the named speaker and the three-/four-strand factorisability subject. It does **not** identify the polyhedron, demonstrate its density model, or certify the other two projects in the talk. In particular, the publication’s authors must not be inferred to be Gömböc coauthors.

## 6. Mathematical evidence inventory

The distinction between an announcement and the requested geometric object remains decisive:

| Required information | Recovered status |
|---|---|
| Named speaker and affiliation | Tancredi Schettini-Gherardini, University of Bonn, explicitly listed by KIAS. |
| Exact talk title and thematic week | Recovered above; the individual presentation day/time remains unconfirmed. |
| Gömböc construction mentioned | Yes, in indexed passages of the institutional abstract. |
| Complete construction author list | Not recovered. |
| Uniform **solid-volume** density | Not established by the recovered passages. |
| Equilibria at the solid’s **own volume centroid** | Not established by the recovered passages. |
| Exclusion of equal vertex masses, another skeleton measure, nonuniform density, or an auxiliary reference point | No recovered statement resolves these alternatives. None is being attributed to the speaker. |
| Full-dimensional convex three-polytope with strict `(1,1,0)` and no degenerate equilibria | No construction/proof recovered with which to check these requirements. |
| Actual maximal-facet, true-edge, and vertex counts | Not recovered. |
| Rational/algebraic coordinates or complete deterministic generator | Not recovered. |
| Exact or directed-rounding centroid and exhaustive equilibrium certificate | Not recovered. |
| Corresponding Gömböc manuscript, DOI, or public supplement | Not identified in the inspected sources. |
| A claimed or proved global minimum | No such claim or proof recovered. |

The unknown entries are **limitations of the evidence obtained**, not findings that the announced construction is invalid or uses the wrong mass model. Conversely, the terminology in an abstract is not enough to fill those entries affirmatively.

## 7. Effect on bounds and priority

**Bounds:** No numerical complexity or admissible construction was recovered from the KIAS lead. It therefore contributes no usable external upper bound and no lower-bound theorem to the present investigation. The coordinator’s supplied interval remains **`28≤C_min≤1374`**. This assignment neither strengthens it nor independently revalidates the mathematical proofs behind it. :contentReference[oaicite:3]{index=3}

**Priority:** The parent’s anonymous lead has become a specific, attributable program announcement. It is no longer appropriate to describe the speaker as unknown. It remains inappropriate to assert either that the user’s C1374 construction is the first explicit homogeneous example or that the KIAS construction has already displaced it. Establishing either conclusion requires the actual competing result and its dated disclosure record. The nominal August event dates, the current search-index contents, an internal construction date, and a later verification replay are different kinds of dates; they must not be silently equated.

**Validity:** Nothing obtained here refutes the KIAS announcement. Nothing obtained here verifies it at the uniform-volume centroid either. This is an unresolved construction-evidence question, not a negative mathematical verdict.

**Exact objects:** This assignment produced no new exact polyhedron, coordinate table, certificate, or successor checkpoint. Accordingly, there is no new mathematical recovery capsule to promote, and no unexpanded or inaccessible external object is being presented as a durable upper-bound witness.

## 8. Most useful continuation

The remaining high-value target is now narrowly specified: a public manuscript, slide deck, recording, or data supplement tied explicitly to **this named KIAS presentation**, with its Gömböc section intact. The first decisive checks are its density measure and reference centre; the next are the full finite geometry, actual feature counts, and all-feature equilibrium proof. The author’s ordinary publication/talk pages, direct arXiv author result set, displayed GitHub repositories, and the subsequent Bonn workshop program have already been followed without recovering that material. Further general Gömböc-history or prize searches would not resolve this gap. Until the named presentation’s technical content is available, the strongest self-contained conclusion is: **speaker and announcement resolved; construction, minimum, and comparative priority unresolved.**
