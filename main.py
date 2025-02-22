import numpy as np

flow_duration = (100.764600 - 0) * 1e6

fwd_packets_length = [0, 0, 227, 0, 214, 277, 1440, 4320, 2880, 2165, 0, 277, 1440, 5760, 3125, 0, 0]  # type: ignore
bwd_packets_length = [0, 1460, 1460, 1323, 107, 0, 0, 0, 0, 0, 869, 0, 0, 0, 0, 309]  # type: ignore
packet_length = fwd_packets_length + bwd_packets_length
total_fwd_packets = len(fwd_packets_length)
total_bwd_packets = len(bwd_packets_length)

total_length_fwd = sum(fwd_packets_length)
total_length_bwd = sum(bwd_packets_length)

fwd_packet_len_max = max(fwd_packets_length)
fwd_packet_len_min = min(fwd_packets_length)
fwd_packet_len_mean = np.mean(fwd_packets_length)
fwd_packet_len_std = np.std(fwd_packets_length, ddof=1)

bwd_packet_len_max = max(bwd_packets_length)
bwd_packet_len_min = min(bwd_packets_length)
bwd_packet_len_mean = np.mean(bwd_packets_length)
bwd_packet_len_std = np.std(bwd_packets_length, ddof=1)

packet_length_min = min(packet_length)
packet_length_max = max(packet_length)
packet_length_mean = sum(packet_length) / (len(packet_length))
packet_length_std = np.std(packet_length, ddof=1)
packet_length_var = np.var(packet_length, ddof=1)

total_length = total_length_fwd + total_length_bwd
flow_bytes_per_second = total_length / (flow_duration / 1e6)
flow_packet_per_second = (total_fwd_packets + total_bwd_packets) / (flow_duration / 1e6)

flow_times = [
    ["FWD", 0],
    ["BWD", 0.086417],
    ["FWD", 0.086485],
    ["FWD", 0.086616],
    ["BWD", 0.176703],
    ["BWD", 0.176751],
    ["FWD", 0.176785],
    ["BWD", 0.176940],
    ["FWD", 0.188321],
    ["BWD", 0.287489],
    ["FWD", 0.294709],
    ["FWD", 0.294880],
    ["FWD", 0.294931],
    ["BWD", 0.381377],
    ["FWD", 0.381463],
    ["BWD", 0.381664],
    ["FWD", 0.381807],
    ["BWD", 0.435476],
    ["BWD", 0.471618],
    ["BWD", 0.472116],
    ["BWD", 0.785937],
    ["FWD", 0.842642],
    ["FWD", 5.303053],
    ["FWD", 5.303234],
    ["FWD", 5.303286],
    ["FWD", 5.303333],
    ["BWD", 5.390196],
    ["BWD", 5.390197],
    ["BWD", 5.390238],
    ["BWD", 5.391033],
    ["BWD", 5.393563],
    ["FWD", 5.452017],
    ["FWD", 100.764600],
]
fwd_times = [time * 1e6 for direction, time in flow_times if direction == "FWD"]
bwd_times = [time * 1e6 for direction, time in flow_times if direction == "BWD"]
flow_times = [time * 1e6 for direction, time in flow_times]

flow_iat = [flow_times[i] - flow_times[i - 1] for i in range(1, len(flow_times))]
fwd_iat = [fwd_times[i] - fwd_times[i - 1] for i in range(1, len(fwd_times))]
bwd_iat = [bwd_times[i] - bwd_times[i - 1] for i in range(1, len(bwd_times))]

flow_iat_mean = sum(flow_iat) / len(flow_iat)
flow_iat_std = np.std(flow_iat, ddof=1)
flow_iat_max = max(flow_iat)
flow_iat_min = min(flow_iat)

fwd_iad_total = sum(fwd_iat)
fwd_iat_mean = fwd_iad_total / len(fwd_iat)
fwd_iat_std = np.std(fwd_iat, ddof=1)
fwd_iat_max = max(fwd_iat)
fwd_iat_min = min(fwd_iat)

bwd_iat_total = sum(bwd_iat)
bwd_iat_mean = bwd_iat_total / len(bwd_iat)
bwd_iat_std = np.std(bwd_iat, ddof=1)
bwd_iat_max = max(bwd_iat)
bwd_iat_min = min(bwd_iat)

fwd_header_lengths = [32, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]  # type: ignore
bwd_header_lengths = [32, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]  # type: ignore
fwd_header_lengths_total = sum(fwd_header_lengths)
bwd_header_lengths_total = sum(bwd_header_lengths)

fwd_packet_per_second = total_fwd_packets / (flow_duration / 1e6)
bwd_packet_per_second = total_bwd_packets / (flow_duration / 1e6)

down_up_ratio = total_bwd_packets / total_fwd_packets

avg_packet_size = total_length / (total_fwd_packets + total_bwd_packets)

fwd_seg_size_avg = total_length_fwd / total_fwd_packets
bwd_seg_size_avg = total_length_bwd / total_bwd_packets

fwd_bulks = [
    [277, 1440, 4320, 2880, 2165],  # No.11, 12, 13, 15, 17
    [277, 1440, 5760, 3125],  # No. 23, 24, 25, 26
]  # type: ignore

fwd_bulks_total = len(fwd_bulks)
fwd_bytes_bulk = sum([sum(bulk) for bulk in fwd_bulks])
fwd_bytes_bulk_avg = fwd_bytes_bulk / fwd_bulks_total
fwd_packets_bulk = sum([len(bulk) for bulk in fwd_bulks])
fwd_packets_bulk_avg = int(fwd_packets_bulk / fwd_bulks_total)
fwd_bulk_duration = (
    flow_times[16] - flow_times[10] + flow_times[25] - flow_times[22]
) / 1e6
fwd_bulk_rate_avg = fwd_bytes_bulk / fwd_bulk_duration

bwd_bulks = []  # type: ignore

subflow_count = 2
subflow_fwd_packets = int(total_fwd_packets / subflow_count)
subflow_bwd_packets = int(total_bwd_packets / subflow_count)

subflow_fwd_bytes = int(total_length_fwd / subflow_count)
subflow_bwd_bytes = int(total_length_bwd / subflow_count)

fwd_init_window = 8192
bwd_init_window = 8192

fwd_act_data_packets = len([packet for packet in fwd_packets_length if packet > 0])
fwd_seg_size_min = min(fwd_header_lengths)

active_time = 5.452017 * 1e6
idle_time = 100.764600 * 1e6 - active_time

print(f"Flow Duration: {flow_duration}")
print(f"Total Fwd Packets: {total_fwd_packets}")
print(f"Total Bwd Packets: {total_bwd_packets}")
print(f"Total Length of Fwd Packet: {total_length_fwd}")
print(f"Total Length of Bwd Packet: {total_length_bwd}")
print(f"Fwd Packet Length Max: {fwd_packet_len_max}")
print(f"Fwd Packet Length Min: {fwd_packet_len_min}")
print(f"Fwd Packet Length Mean: {fwd_packet_len_mean:.6f}")
print(f"Fwd Packet Length Std: {fwd_packet_len_std:.6f}")

print(f"Bwd Packet Length Max: {bwd_packet_len_max}")
print(f"Bwd Packet Length Min: {bwd_packet_len_min}")
print(f"Bwd Packet Length Mean: {bwd_packet_len_mean:.6f}")
print(f"Bwd Packet Length Std: {bwd_packet_len_std:.6f}")

print(f"Packet Length Min: {packet_length_min}")
print(f"Packet Length Max: {packet_length_max}")
print(f"Packet Length Mean: {packet_length_mean:.6f}")
print(f"Packet Length Std: {packet_length_std:.6f}")
print(f"Packet Length Variance: {packet_length_var:.6f}")

print(f"Flow Bytes/s: {flow_bytes_per_second:.6f}")
print(f"Flow Packets/s: {flow_packet_per_second:.6f}")

print(f"Flow IAT Mean: {flow_iat_mean:6f}")
print(f"Flow IAT Std: {flow_iat_std:6f}")
print(f"Flow IAT Max: {flow_iat_max}")
print(f"Flow IAT Min: {flow_iat_min}")

print(f"Fwd IAT Total: {fwd_iad_total}")
print(f"Fwd IAT Mean: {fwd_iat_mean:.6f}")
print(f"Fwd IAT Std: {fwd_iat_std:.6f}")
print(f"Fwd IAT Max: {fwd_iat_max}")
print(f"Fwd IAT Min: {fwd_iat_min}")

print(f"Bwd IAT Total: {bwd_iat_total}")
print(f"Bwd IAT Mean: {bwd_iat_mean:.6f}")
print(f"Bwd IAT Std: {bwd_iat_std:.6f}")
print(f"Bwd IAT Max: {bwd_iat_max}")
print(f"Bwd IAT Min: {bwd_iat_min}")

print(f"Fwd Header Length: {fwd_header_lengths_total}")
print(f"Bwd Header Length: {bwd_header_lengths_total}")

print(f"Fwd Packet/s: {fwd_packet_per_second:.6f}")
print(f"Bwd Packet/s: {bwd_packet_per_second:.6f}")

print(f"Down/Up Ratio: {down_up_ratio:.6f}")
print(f"Avg Packet Size: {avg_packet_size:.6f}")

print(f"Fwd Seg Size Avg: {fwd_seg_size_avg:.6f}")
print(f"Bwd Seg Size Avg: {bwd_seg_size_avg:.6f}")

print(f"Fwd Bytes/Bulk Avg: {fwd_bytes_bulk_avg:.6f}")
print(f"Fwd Packet/Bulk Avg: {fwd_packets_bulk_avg}")
print(f"Fwd Bulk Rate Avg: {fwd_bulk_rate_avg:.6f}")

print(f"Bwd Bytes/Bulk Avg: {0}")
print(f"Bwd Packet/Bulk Avg: {0}")
print(f"Bwd Bulk Rate Avg: {0}")

print(f"Subflow Fwd Packets: {subflow_fwd_packets}")
print(f"Subflow Fwd Bytes: {subflow_fwd_bytes}")
print(f"Subflow Bwd Packets: {subflow_bwd_packets}")
print(f"Subflow Bwd Bytes: {subflow_bwd_bytes}")

print(f"FWD Init Win Bytes: {fwd_init_window}")
print(f"Bwd Init Win Bytes: {bwd_init_window}")

print(f"Fwd Act Data Pkts: {fwd_act_data_packets}")
print(f"Fwd Seg Size Min: {fwd_seg_size_min}")

print(f"Active Time: {active_time}")
print(f"Idle Time: {idle_time}")
