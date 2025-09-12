import numpy as np
import matplotlib.pyplot as plt

# x axis: Byzantine proportions
props = np.array([0,5,10,15,20,25,30,33])

# Replace these arrays with your measured/estimated values
tps = {
    "baseline": np.array([1000]*8),
    "equiv_single": np.array([1000,995,990,980,965,940,900,880]),
    "equiv_collude": np.array([1000,950,900,820,720,620,520,480]),
    "delay_border": np.array([1000,980,960,920,880,820,700,640]),
    "delay_trigger": np.array([1000,940,860,760,640,500,360,320]),
    "dos_single": np.array([1000,990,980,970,940,900,820,780]),
    "dos_collude": np.array([1000,930,820,680,520,360,220,180]),
    "net_loss": np.array([1000,985,970,940,900,840,760,720]),
}

p95 = {
    "baseline": np.array([300]*8),
    "equiv_collude": np.array([300,380,460,560,700,900,1150,1300]),
    "delay_border": np.array([300,420,540,700,920,1150,1350,1500]),
    "delay_trigger": np.array([300,480,700,1000,1500,2200,3000,3500]),
    "dos_collude": np.array([300,450,650,900,1300,1900,2600,3200]),
    "net_loss": np.array([300,320,340,380,420,500,620,700]),
}

p99 = {
    "baseline": np.array([450]*8),
    "equiv_collude": np.array([450,520,620,760,900,1200,1600,1800]),
    "delay_border": np.array([450,620,800,1100,1500,2000,2600,3000]),
    "delay_trigger": np.array([450,800,1100,1600,2400,3400,4500,5200]),
    "dos_collude": np.array([450,700,1000,1400,2000,3000,4200,5200]),
    "net_loss": np.array([450,480,520,600,700,900,1100,1250]),
}

commit_ratio = {
    "baseline": np.array([1.0]*8),
    "equiv_single": np.array([1.0,0.999,0.998,0.996,0.99,0.98,0.95,0.92]),
    "equiv_collude": np.array([1.0,0.995,0.985,0.96,0.91,0.85,0.72,0.65]),
    "delay_border": np.array([1.0,0.999,0.998,0.997,0.995,0.992,0.98,0.97]),
    "delay_trigger": np.array([1.0,0.998,0.995,0.99,0.985,0.97,0.95,0.94]),
    "dos_collude": np.array([1.0,0.995,0.99,0.98,0.95,0.92,0.85,0.8]),
    "net_loss": np.array([1.0,0.999,0.998,0.996,0.994,0.99,0.98,0.97]),
}

# Plot TPS
plt.figure(figsize=(8,4.5))
for k,v in tps.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("TPS vs Byzantine proportion (example/estimated data)")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("TPS (tx/s)")
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
# plt.show()
plt.savefig("tps.png")

# Plot p95 and p99 in separate figures
plt.figure(figsize=(8,4))
for k,v in p95.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("p95 latency vs Byzantine proportion (ms)")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("p95 latency (ms)")
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
# plt.show()
plt.savefig("p95.png")

plt.figure(figsize=(8,4))
for k,v in p99.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("p99 latency vs Byzantine proportion (ms)")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("p99 latency (ms)")
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
# plt.show()
plt.savefig("p99.png")

# Plot committed-correct ratio
plt.figure(figsize=(8,4))
for k,v in commit_ratio.items():
    plt.plot(props, v, marker='o', label=k)
plt.title("Committed-correct ratio vs Byzantine proportion (example data)")
plt.xlabel("Byzantine proportion (%)")
plt.ylabel("Committed-correct ratio")
plt.ylim(0,1.02)
plt.grid(True)
plt.legend(fontsize='small', ncol=2)
plt.tight_layout()
# plt.show()
plt.savefig("ccr.png")
