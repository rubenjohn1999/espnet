#!/usr/bin/env python3

# Referred from data_prep.py in jv_openslr35 in ESPnet
# https://github.com/espnet/espnet/blob/master/egs2/jv_openslr35/
# asr1/local/data_prep.py


import argparse
import os
import random
import pickle


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", help="downloads directory", type=str, default="downloads")
    args = parser.parse_args()

    # tsv_path = "%s/mono_index.tsv" % args.d
    #
    # with open(tsv_path, "r", encoding="utf-8") as inf:
    #     tsv_lines = inf.readlines()
    # tsv_lines = [line.strip() for line in tsv_lines]

    spk2utt = {}
    utt2text = {}
    files = os.listdir(args.d)
    for file in files:
        fid = file
        spk = 'mono'
        text = 'mono'
        path = "%s/%s" % (args.d, fid)

        if os.path.exists(path):
            utt2text[fid] = text
            if spk in spk2utt:
                spk2utt[spk].append(fid)
            else:
                spk2utt[spk] = [fid]

    spks = sorted(list(spk2utt.keys()))

    spks_by_phase = {"mono": spks}
    flac_dir = "%s" % args.d
    sr = 16000
    for phase in spks_by_phase:
        spks = spks_by_phase[phase]
        text_strs = []
        wav_scp_strs = []
        spk2utt_strs = []
        num_fids = 0
        for spk in spks:
            fids = sorted(list(set(spk2utt[spk])))
            num_fids += len(fids)
            utts = [spk + "-" + f for f in fids]
            utts_str = " ".join(utts)
            spk2utt_strs.append("%s %s" % (spk, utts_str))
            for fid, utt in zip(fids, utts):
                cmd = "ffmpeg -i %s/%s.wav -f wav -ar %d -ab 16 -ac 1 - |" % (
                    flac_dir,
                    fid,
                    sr,
                )
                text_strs.append("%s %s" % (utt, utt2text[fid]))
                wav_scp_strs.append("%s %s" % (utt, cmd))
        phase_dir = "data/%s_ml" % phase
        if not os.path.exists(phase_dir):
            os.makedirs(phase_dir)
        text_strs = sorted(text_strs)
        wav_scp_strs = sorted(wav_scp_strs)
        spk2utt_strs = sorted(spk2utt_strs)
        with open(os.path.join(phase_dir, "text"), "w+") as ouf:
            for s in text_strs:
                ouf.write("%s\n" % s)
        with open(os.path.join(phase_dir, "wav.scp"), "w+") as ouf:
            for s in wav_scp_strs:
                ouf.write("%s\n" % s)
        with open(os.path.join(phase_dir, "spk2utt"), "w+") as ouf:
            for s in spk2utt_strs:
                ouf.write("%s\n" % s)
