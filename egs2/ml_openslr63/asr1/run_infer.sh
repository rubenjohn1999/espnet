#!/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

train_set="train_ml"
train_dev="dev_ml"
test_set="test_ml"

./asr.sh \
    --ngpu 1 \
    --gpu_inference true \
    --skip_data_prep true \
    --skip_train true \
    --asr_exp exp/asr_train_asr_conformer_s3prlfrontend_hubert_fused_raw_ml_bpe150_sp \
    --lm_exp exp/lm_train_lm_ml_bpe150 \
    --feats_type raw \
    --feats_normalize utt_mvn \
    --train_set "${train_set}" \
    --valid_set "${train_dev}" \
    --test_sets "${train_dev}"