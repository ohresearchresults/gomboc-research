# material-d1d4ee74b946

Historical AI scientific source/proof material. Statements retain their original scope; this is not an independently reviewed theorem.

Public derivative: internal-record-identifiers-replaced; runtime-path-removed.

---

"""TREE253_K2_CHECKPOINT40_RECOVERY_METHODS_V1, complete source capsule.

Reconstruction: save this literal complete material as recover_methods.py in
an empty working directory, and run python -S recover_methods.py.
Verification: python -S recover_methods.py --verify.
Both check every embedded byte count/hash and compile all four complete source
units without importing numerical packages. --verify does not overwrite.
Expected marker: TREE253_K2_CHECKPOINT40_RECOVERY_METHODS_EXACT_PASS 4.
Embedded raw input and all reproduced file pins are literal below.

Dependency: recover the complete shared code from [internal-source-reference]
(15320 bytes, SHA bb7e5afb92c0708251528299eb10f72cb05e4d7450a34d42d73a245adcfdf254),
using python -S recover_shared_code.py in this same working directory. No code
is fetched from the network. Four complete helper programs here supplement,
and do not modify, its thirteen already-preserved files.

Frozen proof replay, requiring no solver: follow the complete data-part map
and commands in [internal-source-reference] (25213 bytes, SHA
32d9113122c34015de2497bec5704b9bc680d5689ddc4c0bcd5474d8f338729d).
Then run python -S build_capsules.py 0 1 2 3 5 6 7 8 9.
It rechecks all exact inputs, reproduces the nine case files byte for byte,
and refuses to replace different existing data. Each line begins
PACKED_EXACT_NATIVE INDEX followed by bytes and SHA; the expected case pins
are CASE_PINS below. The decoded input JSON files, report JSON and stdout
files have exact pins in the cited proof and in each complete native header.
Thus no unpreserved floating proposal is needed to reconstruct the findings.
The packer writes packed_manifest.json from those exact headers; its pin is
MANIFEST_PIN below and can be verified by python -S recover_methods.py --pins.

Optional numerical-method reproduction, NOT a proof by itself:
  python shared_code/rebuild_missing.py
  python shared_code/rebuild_preserved.py
  python shared_code/quantize_rebuilt.py 0 1 2 3 5 6 7
  python -S build_capsules.py 0 1 2 3 5 6 7
The two first programs encode every selected incidence[private-runtime-path]
input literally, start the unchanged original locators with zero vectors,
and use two child processes with each BLAS/OpenMP thread count fixed to1.
They produce complete candidate_rR.json inputs in iI_rR or iI_rR_s01 folders.
Their status-file ordering and wall-time log fields are not deterministic
mathematical inputs. Quantization uses the literal ordered powers
12,14,16,18,20,24, NumPy rint, and exact Bareiss plus rational LDL acceptance.
All other nondefault numerical parameters and the complete original source
are in the shared dependency. Native8/9 were not numerically regenerated in
this recovery: their four frozen certificates were read from their complete
immutable native capsules instead. No false failure/feasibility inference is
made when a numerical candidate is absent or fails exact rounding.

Observed numeric environment is CPython3.13.5, NumPy2.3.5, SciPy1.17.0,
OpenBLAS0.3.30 on x86_64 Linux, OPENBLAS_NUM_THREADS=1, OMP_NUM_THREADS=1,
no random seed because no random input. Exact frozen verification uses only
the Python standard library. Numerical bitwise replay is not a prerequisite
for the stored integer proofs. All36 regenerated accepted integer records
matched their intended original inputs and both missing native00/01 whole
capsules matched their original intended SHA-256, correcting an intermediate
journal assertion based on stale input metadata. The old broken00 fragments
[internal-source-reference] and [internal-source-reference] are excluded.
LZMA preset9 is explicit in the complete packer: using default preset6 gives
different compressed bytes even though the decoded integer object is equal.
This is a source-preservation/method capsule, not a new root exclusion.
"""
from pathlib import Path
import base64,zlib,hashlib,json,sys
assert __debug__
RAW_PIN=[9119, 'c5a720620358f38258d83e01c89108e2c8e695f6f86aaf6419211aa0f40f7658']
FILE_PINS={'shared_code/rebuild_missing.py': [1757, '89a797d1312f944dd53d962a73d9be415c02b4be9b30a7d58a4182be9cd6b71e'], 'shared_code/rebuild_preserved.py': [1789, '0c369274836a7bdd186dadee3ba999575f9486274a5ee5bd98ad271ce16f93da'], 'shared_code/quantize_rebuilt.py': [2478, '43db916903157269b17a1e2dba0088015d6b40db947e668873a9422090d49879'], 'build_capsules.py': [2784, 'a1ee4d3abeb4f19aefb5072ddd63163db03e23e1b655350d2afc195e5c5667ba']}
CASE_PINS={'case_00.txt': [29354, '960b9d9f570c954ea8c57334f7e42be187a53a9ed08076b67d5b439208b6ca65'], 'case_01.txt': [29156, '010ac21d4e32eb0c342ef2cb988398a70e312bfca0254dfe214ea006f7c3510f'], 'case_02.txt': [15880, '60758b9d5b0200bd7e2aaccedbf286a5692c98e119c87a5c3a9312deee8a04c9'], 'case_03.txt': [14309, '1c0b77e02863c5c0862ce67864dd8e379c343360a5fc97d33fa7005d277e378b'], 'case_05.txt': [11121, '38d40db498f315da9fdbc74a80d5e8e3193e9e4f605ba89c93ebd62ce73ca73d'], 'case_06.txt': [11688, 'd459310e83380f7d9085af514fdf097c312e7c87249684b4313704ba867c749d'], 'case_07.txt': [11335, 'e4117f52a47f28968c87b3125999e94046cff17afb025b2635f78cb0c271d808'], 'case_08.txt': [6253, '1a80d70438d18b72d06a860ffe1e2f814c8cf7d858f4af32b4754a457927d6b1'], 'case_09.txt': [6261, '28c9f2eed87f08cb09b1ab9dbe6b5667a61163d73f3739d22e5fcdf8bfae1d84']}
MANIFEST_PIN=[8700, '5619703ffa0618a737079e141d464468a594d6c37eb15620f9117dbecf56e03f']
DATA=(
 'c-rk*?Qhyh8vlNOg;i<Kb~<$fP17DZS7L*+MVkU5q_?{SS;iiMH(+~b#w0YC|NWk4Ucd&@?VfbfeQ2YCJ@d@-'
 'HqXm%hQ}AvGF>EL92LA=Q0^7$7p)gJ@^28ucUGJ)iv<<bq7P9ltSl1gidtzV=q+XNU6g`bQI=R@PE)3-;yI1)U^*`a&U-'
 'i6HK!a&tTKz|QFcoci_arQlaS{ni>bwEoUbTb13@aR2zdgtVv)x1n$Ut~3C-'
 'd)u<GU3Y>|T=*{xONpox_;D=U|jrE#>dc)nPnX51<{NSUrdEW8wv(um=R5eD3psW;h-'
 '<x3zE^F=zf(q)k|VGZE*Cets|h||*(66eL5%p;C;<aeHDWbtJg5iVF63&P83!Sa}LPWYM=K_A3Di;A0U*zb>g<mZIpEM3qrbUj9;'
 'u8!*!;E7D!Was@(;3Mg4TYD$Y6Kdap?K2C^cOKjpqoQP)<)CaYDVGIz9tZ~w!#ld>{)m;7a0(nFku&Z)Hi5sE?Yb}Ro14sbJ>UaO'
 '9anKJ(yYRDyrB4M4D>*Y=G#*k@#gd)NpC3^jyq8+R}ll}J73(^O=iKr(r+GpvC^6K<%550(FLd0D;RmzP}5U?x)wBIELx*%9J-'
 '%_C#>>=-'
 ')O#XO}(hVU3Q%E?~Ud=_unw+o|PXy`0q3WLr}VBTHPt^pRxjW*Gb{=!Dy4Du*u+oweqK9tH=$1IBq8P4~kS#7SS5QDe)hl&LG&A5'
 'X;;jPtJ1i43~o#%;tsVxxi_)bOzyc2fT<0_!L~|*jxaUh$Y~7h_ZCHhV&BABEKyu<d^Ld$Bq_)GNsa%3OyQSf=i-'
 '_HU$4cn)xW_r5(nUiF5{$E+APk2J8yi%*t|MIUCzw!$R2bhm;HMxUD$PAZtpxUBM{Ew&AVb6xTCQ*Nn@g_F$kQYwGWcVKhoY++z@'
 'Rrky&5nTan$6<@hCb<ZNsDdv;!V?<X8-7Wi#)5qGi6CWeh!3=q=hw38Ts#Q?SguhKjkCmA-hKvMX(6|)QbU}&z>dMBvt@9+H2vLr'
 'hkoZ3FH&&`m)(IvOsBKjVgYF=xs8DeZ_|5h1St_VjRjKDG9+fpR;>KFGGIz^G4eyw&f^-'
 'ZL6#a9YO<bD{GES`+OOT1H;v2jqkc^FOe77eu&}DR2w+m*Wj<ST?X6N+QViA#yT;IoMPKAEgbl~+AG)a7{rd~p6fe$7Y+_Pz#MUc'
 '6B1q0Q{q9yhp3rikN9K*`3q{~KIGdadZRedYO_-_?0xX-*IFC070=?wBKg@Vj&aLBki0`<7ez#-BsT;<joq2v`x#<`YuhgcWXS-'
 'IGfpkQj_jE{8{T^ZLbsfc7^Yz#YN(Y>$wizn-x{m-sVPywWcx{hBj6<5V$4lzO*L~bmc6xyap#oD(=!ystBeG~rN49`CX=RXhn-'
 'QMWrIJ_A4e+znHuRZF14#Lk3o9I$0i=;0<$=1w_-iNrEVUhDxq&d_@y%lPUiNpk<DwuaI3`;Zz3{>TktSWKjK~^jwlAkI96lhQkW'
 'PF?Is)ja|fo!U^c_82^BvQE$-5Z}y^91b2?&tjufWa|s*~1S<HFj@$dZIfcHgpeh52O=EJ_Mhr@c-eu5Ui?ulE(3|>8VNza+N!$-'
 '0!}e%E^}~z0!0gX~b@UpYBXCC?NZiCmuw-'
 'H$g>LwA&(Xf=Ufn%YpBs3ea4FU%FSLZtth?ygj(Oz6`=n_u?WLLb+3$S!f@)>S>>oThp^vyyQCFIA!G8gZBB)K_?7;X`hdD6d6HB'
 'TS>D;$>*|o>eaf1D`#OJ2V27s6EzHd-wwlNlxAUQw`!#&3==vnZ^O_qk^Sot%XsRx6bw*-'
 'mSUJKVShnM1Y;i9vKlv96Zc82brjH&z%T)6pa8%d)&1%P8#h(gUr_!9c~Jppum32aWv5>#bWeoRqKcp|7^Pnj+uqWQ0w4oCs)4FO'
 '&iAR9YtZ~7@Ju-'
 '%Rq&Jr#E@D5XD>UKRuspy089~60IXdNxf$JJ^BAH(O@M#MhSC5FF($Y2nZ(>OeAx=5Z_)Q6k0n3^j{R)0mUQtv=QP`ZdtEJw1QmM'
 '#o0qY~xfVDL`f1A1ju><Yz5fcXmKYlLXEOkjiZz}9vSKr~3!`w_psZaYgQDaiVhgiwvX8+q_;U<CxNP_Q$K%%H7RI%l25FKL@{YW'
 'BNe#NSoHyhxIfeSw*k5p%{6sHk))yQi1|~rGrcQX6Z-W5k+rv6Mk<;fU-aRt`DKhB)3rdFXG@7JwLK>%}@t!n~N%I6!;OqI-suel'
 '(x_0g!3U|+Rg<0MK(s5*s3-'
 'h~bnb<&V*<Da3ZqPWLnAXwS0gcf3j73;JaV?aSjgjhLQj3c%Y?Sei;9nv{!21U<h16pQKWq;hXzgofW~YzoQ^+3Kll{CB6{?UQH|'
 '!lOkyLSW1qsgVO1i^ZQ?X<L$6{N<!j;;YjO}V?2NdI{^5~uzoag)Oxs`x(^H~TMh>|0r9SlAOpMqigGVJw7s`_948h#Fj-HUF}vF'
 'm)KKgX&{PkdmPW-'
 '%g@nA($l1Xbks>MW&VaL3tts}#JcLlqe$J|j_)LTy4h>dBtKObJfQZbQl3m!G7H_57^xWJ81Rh%4BcjO%c4;vO}Rj^tVwh$OHBa#'
 '(eG;(8*7D!A``-N$td)Y2Br@X7*r(&6)TCZx*h2~?g%S-6O%5Gy#meX}PABnY-'
 '{>G=2LcZje8+Ez^J?mn;<>NfNj%W2EqhWZ^amNW7jWqBuErQD3TSW@Z3f&Hk!fnoo;*Fo@c(e7SCAQ0FUqTDV01=z+jecnCWKa%c'
 'bqdBs`E1W8KM6}P(gTbgK1P%|72zPaUm~Jf=rI2((!0+jjN_!l~?)5crF+3%!>J}aZ&{rSZL%=++@EQ`}Q~y)Y8(jh18nrL`KV1W'
 'gZhj^2tBl&0qhP3^_eHyB7#og&#w*AheD?e`z}eI{`>(-f9sipLvWW%mtAntqd-}U-'
 'JT`7$)#%qKzINAulY6*S4%SiW6d<WWpkPzD0jJ&G;Ch7aM#eibYw&AYozxK!{CM5H9089}@KZ3X^CCya5ePr0JJ@rN1FXE-'
 ')Gv85!hnK5by%piwte`gP#@q&fNoG;s_1XHfqhoKg;;oc!CT9dW7SHmdqiDZEGL1XB`vogo~cA%8w7XwDplWSZs8@sGz0L?3{snw'
 '3p1_YqhbtYeHX4lQpP32j_u7#K<OY)L#)vpw|0={i$GqaK$U=+5E|u^Z^e674#2T;S!ziD_-'
 'z2~YSiv^+QW`Nc8(!cx1G6y(k3s*@U}N8r*5)J((N-'
 '*fbIYT1KlPXBi1hZQbP+5NNtovKK0AKUCN3w`eHTDC>+Z8oq;wI{s6U)gK8*VCjQ=i7ArGZ^zr(Ts9r0-'
 'm^*pC80~S<@Hyl(V)1;R7qO2?!*p$Vd~qb`nb{^49#PU$h}Z_<3EmsJUJg~<vG1q0Y$9;RuXK@O_o@!elXq{(n9ywHKOP<Bpk}s8'
 '8AOlW9|XN0FWXmP@A^|X`Zx^Qoh!R#Hy~;Ip9XuQPv*W3{^KKMtSa$p)ahT3+&$F#U*ouEAeuR{%F9VvoFzZGy@zp(IwND9@d2D{'
 'UY@@k(A)v&nK}T42{Nx-'
 '+O=!g>X~0d#)E5WM|H*f&kpJ;8aBaDETXJ_rk3(5zg}Q6ef1ZMs^7ME?=tlE>yfjJ9>V*aLHXx?QwCcB(>u3=Gt9hd;c~`E<v~;|'
 'Q{g}c5}~qGm?Ou;-N8LtAp=lmo*KYw*_|E(@d&W^JnZ)_f3-=)bj@P?sxjI53Fp9t$>wUg?qCJUzwTl!=db)sRJ-'
 'C)hIBTDbo#wOT|sKjJL*2uBez|w)+HfC)|ESoT8lJY%o4e5k=VC(etd)(_1j~*T&f~wZGO%C-'
 'YqNLvRUtErcb`94>varbla)q1oS@g?wdMllQdicpH29D1JB<(=J$^Iy<>iJ$267jd++>T_s*@W|1Z1f)8GCB`<DAm'
)
def pin(b):return [len(b),hashlib.sha256(b).hexdigest()]
if __name__=='__main__':
    assert sys.argv[1:] in ([],['--verify'],['--pins'])
    root=Path(__file__).resolve().parent
    if sys.argv[1:]==['--pins']:
        for name,p in CASE_PINS.items():assert pin((root/name).read_bytes())==p
        assert pin((root/'packed_manifest.json').read_bytes())==MANIFEST_PIN
        print('TREE253_K2_CHECKPOINT40_REPACK_PINS_PASS',len(CASE_PINS))
    else:
        raw=zlib.decompress(base64.b85decode(DATA));assert pin(raw)==RAW_PIN
        files=json.loads(raw);assert set(files)==set(FILE_PINS)
        for name,text in sorted(files.items()):
            b=text.encode();assert pin(b)==FILE_PINS[name]
            compile(text,name,'exec')
            p=root/name
            if sys.argv[1:]:assert p.read_bytes()==b
            else:
                if p.exists():assert p.read_bytes()==b
                p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(b)
        print('TREE253_K2_CHECKPOINT40_RECOVERY_METHODS_EXACT_PASS',len(files))
