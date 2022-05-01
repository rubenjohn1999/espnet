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

    tsv_path = "%s/line_index_all.tsv" % args.d

    with open(tsv_path, "r", encoding="utf-8") as inf:
        tsv_lines = inf.readlines()
    tsv_lines = [line.strip() for line in tsv_lines]

    spk2utt = {}
    utt2text = {}

    # Parse through the openslr files
    for line in tsv_lines:
        l_list = line.split("\t")
        fid = l_list[0]
        spk = fid.split("_")[1]
        text = l_list[1]
        text = text.replace(".", "")
        text = text.replace(",", "")
        text = text.lower()
        path = "%s/%s.wav" % (args.d, fid)
        if os.path.exists(path):
            utt2text[fid] = text
            if spk in spk2utt:
                spk2utt[spk].append(fid)
            else:
                spk2utt[spk] = [fid]

    # Parse through monolingual data
    files = os.listdir(args.d)
    for file in files:
        if (not file.startswith('mlm')) and (not file.startswith('mlf')) and file.endswith('.wav'):
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

    # Reading list of test speakers
    open_file = open("/home/ubuntu/espnet/egs2/ml_openslr63/asr1/local/test_speakers.pkl", "rb")
    test_spks = pickle.load(open_file)
    open_file.close()

    # Reading list of dev speakers
    open_file = open("/home/ubuntu/espnet/egs2/ml_openslr63/asr1/local/dev_speakers.pkl", "rb")
    dev_spks = pickle.load(open_file)
    open_file.close()

    set_difference = set(spks) - set(test_spks) - set(dev_spks)
    train_spks = list(set_difference)

    # Remove mono from train and dev
    train_spks.remove("mono")

    # random.Random(0).shuffle(train_dev_spks)
    # num_train = int(len(train_dev_spks) * 0.9)
    # train_spks = train_dev_spks[:num_train]
    # dev_spks = train_dev_spks[num_train:]
    mono_spks = ["mono"]

    spks_by_phase = {"train": train_spks, "dev": dev_spks, "test": test_spks, "mono": mono_spks}

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
            if phase == "test" and num_fids > 800:
                curr_num_fids = num_fids - 800
                random.Random(1).shuffle(fids)
                fids = fids[:curr_num_fids]
            utts = [spk + "-" + f for f in fids]
            utts_str = " ".join(utts)
            spk2utt_strs.append("%s %s" % (spk, utts_str))
            if phase == "mono":
                for fid, utt in zip(fids, utts):
                    cmd = "ffmpeg -i %s/%s -f wav -ar %d -ab 16 -ac 1 - |" % (
                        flac_dir,
                        fid,
                        sr,
                    )
                    text_strs.append("%s %s" % (utt, utt2text[fid]))
                    wav_scp_strs.append("%s %s" % (utt, cmd))
            else:
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