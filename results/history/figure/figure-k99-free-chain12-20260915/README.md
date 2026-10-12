# K99: exact twelve-link ascent chain in free space, not a polyhedron

The source entry and complete 2771-byte free_chain12.py are preserved. The author reports a rational 12-link strictly ascending chain between the exact K99 inlet111 and outlet150, at K99's own centroid. The existing energy inequality rules out at most11 links; this demonstrates sharpness for an unconstrained chain.

The chain violates retained K99 supports3,17,73,99. It is NOT a convex-body construction or an admissible critical-region repair. Merely adding enough links does not solve convex embedding. The generic angular criterion and its argument are retained in journal-entry.md with this scope.

Exact input recovery uses the already preserved 28-file package at ../figure-nh72-critical-energy-20260915/source. Run its REPLAY.py --out parent-output --stage BASE from its source directory, with a new output directory. Then run free_chain12.py with that output's BASE/B.json and a new report path. Input and expected output hashes are in the receipt and journal extract. Exact computation uses Python's standard library with assertions enabled.

Source/dependency hashes, syntax and readbacks were verified locally. The monitor did NOT repeat the scientific calculation or independently verify the generic theorem. The C624 construction record is unchanged.
