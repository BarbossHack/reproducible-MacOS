# Notes

<https://theapplewiki.com/wiki/Keys:Cheer_25A354_(Mac16,10)>

```bash
curl -L "https://updates.cdn-apple.com/2025FallFCS/fullrestores/093-37622/CE01FAB2-7F26-48EE-AEE4-5E57A7F6D8BB/UniversalMac_26.0_25A354_Restore.ipsw" -o UniversalMac_26.0_25A354_Restore.ipsw

brew install blacktop/tap/ipsw

ipsw extract --files --dmg sys --lookup UniversalMac_26.0_25A354_Restore.ipsw -o ./extract/

ipsw fw aea ./extract/25A354__MacOS/090-87790-616.dmg.aea --key-val "base64:vftoDg1PNe1a3GUyeup9lKrzIspNicLYdT2mEOjCkto=" -o ./decrypted
# OR
aea decrypt -i ./extract/25A354__MacOS/090-87790-616.dmg.aea -o ./decrypted/090-87790-616.dmg -key-value 'base64:vftoDg1PNe1a3GUyeup9lKrzIspNicLYdT2mEOjCkto='
```

<https://github.com/kinnay/AEA>

<https://github.com/dhinakg/aeota>
