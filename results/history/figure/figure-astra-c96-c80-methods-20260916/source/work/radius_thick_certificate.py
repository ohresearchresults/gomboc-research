"""Exact quarter-radius certificate for the larger, nonwinning thick body."""
import hashlib,json
from fractions import Fraction
from radius_certificate import ROOT,metric


def main():
    row=metric('capped-bulk-exact','67c1f2a075a3b55b04bebfa76d719edcab24b6ae854a5ac75f775b9c9801b086')
    assert 16*Fraction(row['ratio_squared'])>1
    row['ratio_greater_than_one_quarter']=True
    out=ROOT/'work/radius-thick-certificate.json'
    out.write_text(json.dumps(row,sort_keys=True,indent=2)+'\n')
    print('EXACT_THICK_RADIUS_GREATER_THAN_QUARTER_PASS',hashlib.sha256(out.read_bytes()).hexdigest())


if __name__=='__main__':main()
