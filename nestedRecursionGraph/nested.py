import matplotlib.pyplot as plt


def mcCarthy91_trace(n, trace: list):

    trace.append(n)

    if n > 100:
        return n - 10
    else:
        return mcCarthy91_trace(mcCarthy91_trace(n + 11, trace), trace)


n = 99
trace = []
mcCarthy91_trace(99, trace)
print(trace)

plt.plot(range(len(trace)), trace, marker="o")
plt.title(f"McCarthy 91 Trace (n={n})")
plt.xlabel("Call Depth")
plt.ylabel("n Value")
plt.yticks(range(min(trace), max(trace) + 1, 1))
plt.grid(True)
plt.axhline(100, color="red", linestyle="--", label="Threshold (n=100)")
plt.legend()
plt.show()
