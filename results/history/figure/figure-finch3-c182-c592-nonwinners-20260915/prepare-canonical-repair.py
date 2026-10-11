import ast,base64,hashlib,json,lzma,re
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).parent
JOURNAL=Path("/REDACTED_HOME/.pro-research/runs/run_-kjrDuYVMzeTQ9tyWn464e75/research-journal.md")
sha=lambda b:hashlib.sha256(b).hexdigest()
original=(ROOT/"SOURCE_CAPSULE.b85").read_text()
if len(original)!=59545 or sha(original.encode())!="776bd3a4fa0abe64ede23fde3078f938a7df8d58117e320df8504ce428c6bccc":raise ValueError("Original capsule pin")
journal=JOURNAL.read_bytes();text=journal.decode()
sections=re.findall(r"^## Recovery capsule part ([1-6])/6 — FINCH3_COMPLETE_TEN_NONWINNERS_AND_METHODS\n(.*?)(?=^## 2026-|\Z)",text,re.M|re.S)
if [int(n)for n,_ in sections]!=list(range(1,7)):raise ValueError("Canonical part count/order")
parts=[];receipts=[]
for n,body in sections:
    b=re.findall("^"+chr(96)*3+r"(?:b85|text)\n(.*?)^"+chr(96)*3,body,re.M|re.S)
    if len(b)!=1:raise ValueError("Part block ambiguity")
    i=int(n);actual="".join(b[0].split());expect=original[(i-1)*10000:i*10000]
    prose=re.search(r"(?:bytes|ASCIIbytes)/SHA([a-f0-9]{64})",body)
    parts.append(actual);receipts.append({"part":i,"actualChars":len(actual),"actualSha256":sha(actual.encode()),"expectedChars":len(expect),"expectedSha256":sha(expect.encode()),"actualMatchesOriginal":actual==expect,"proseSha256":prose.group(1)if prose else None})
if not all(r["actualMatchesOriginal"]for r in receipts[:5]):raise ValueError("Earlier source parts changed")
if receipts[5]["actualMatchesOriginal"]:raise ValueError("Fault no longer present; do not prepare stale repair")
payload="".join(parts)
decode_error=None
try:
    decoded=lzma.decompress(base64.b85decode(payload))
    decode_error="Decoded unexpected map "+str(len(decoded))+" bytes/SHA"+sha(decoded)
except Exception as e:decode_error=type(e).__name__+": "+str(e)
fixed="".join(parts[:5])+original[50000:]
if fixed!=original:raise ValueError("Exact replacement failed")
correct_data=lzma.decompress(base64.b85decode(fixed))
if len(correct_data)!=210036 or sha(correct_data)!="0ba9975c3b9c374c8b2b51f6cba4c2ec0328752136a1e93813fb6dd20eb26ad6":raise ValueError("Restored map pin")
tick=chr(96)*3
draft="# DRAFT — exact Finch3 part6 correction; not applied to the live journal\n\nThe canonical part6 at2026-09-15T20:31:06.665Z contains12129 normalized characters, not the declared9545, and does not equal the original immutable worker capsule tail. Parts1–5 are byte-identical to that original. This is a source-transfer defect, not a change to the mathematical objects. The full44-source package remains safely preserved locally and in the worker's accepted immutable result.\n\nUse a new dated correction declaring the payload below to replace the earlier part6. Do not rewrite historical bytes or accept the bad combined payload as complete. Correct per-part hashes: part4="+receipts[3]["expectedSha256"]+", part5="+receipts[4]["expectedSha256"]+", part6="+receipts[5]["expectedSha256"]+". Earlier prose pins for these parts are wrong. Part6 is the original exact interval[50000,59545).\n\n"+tick+"b85\n"+"\n".join(original[i:i+100]for i in range(50000,59545,100))+"\n"+tick+"\n\nConcatenation with the unchanged originalparts1–5 gives59545chars/SHA776bd3a4fa0abe64ede23fde3078f938a7df8d58117e320df8504ce428c6bccc; LZMA-decoded map210036bytes/SHA0ba9975c3b9c374c8b2b51f6cba4c2ec0328752136a1e93813fb6dd20eb26ad6. Existing original integer-delta recipes reconstructall44pinnedfiles; no code, coordinate or coefficient was inferred.\n\nAuthority: accepted resultasg_9_3jUNaB9fDmUrfQOxs-5B7l SHA243b10b026bbadf9b085000d4490d02db4f2273c1836e07188b407ad662a66ee, matchedbackend/sourcecapsule. Mathematical evidence staysauthorreported; these remainnonwinners andC622remainsaccepted.\n"
def write(name,b):
    with(ROOT/name).open("xb")as f:f.write(b)
    if(ROOT/name).read_bytes()!=b:raise ValueError("Readback")
write("CORRUPT_CANONICAL_PART6_2035.b85",parts[5].encode())
write("EXACT_ORIGINAL_PART6.b85",original[50000:].encode())
write("FINCH3_CANONICAL_REPAIR_DRAFT.md",draft.encode())
receipt={"at":datetime.now(timezone.utc).isoformat(),"canonicalJournalBytes":len(journal),"canonicalJournalSha256":sha(journal),"parts":receipts,"badCombinedChars":len(payload),"badCombinedSha256":sha(payload.encode()),"badDecode":decode_error,"local44SourcePackageIntact":True,"exactOriginalTailRecovered":True,"exactReplacementRestoresPinnedMap":True,"replacementChars":9545,"replacementSha256":receipts[5]["expectedSha256"],"draftBytes":len(draft.encode()),"draftSha256":sha(draft.encode()),"canonicalJournalChanged":False,"state":"EXACT_RECOVERY_SAVED_CANONICAL_REPAIR_PENDING"}
write("canonical-corruption-receipt.json",(json.dumps(receipt,indent=2)+"\n").encode())
print(json.dumps(receipt))
