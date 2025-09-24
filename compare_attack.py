import re, pandas as pd, matplotlib.pyplot as plt

def parse_log(path):
    heights, tps = [], []
    with open(path) as f:
        for line in f:
            m = re.search(r'block\.BlockHeight:(\d+).*平均每秒交易处理量 \(平均 TPS\):(\d+)', line)
            if m:
                heights.append(int(m.group(1)))
                tps.append(int(m.group(2)))
    return pd.DataFrame({'height':heights,'tps':tps})

baseline = parse_log('baseline.log')
silence  = parse_log('silence_attack.log')

plt.plot(baseline['height'], baseline['tps'], label='No Attack')
plt.plot(silence['height'],  silence['tps'],  label='Silence Attack')
plt.xlabel('Block Height')
plt.ylabel('Average TPS')
plt.title('PBFT TPS Comparison')
plt.legend()
plt.grid(True)
plt.savefig('tps_compare.png', dpi=200)
plt.show()
