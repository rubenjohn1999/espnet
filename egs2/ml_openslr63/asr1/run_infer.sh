#!/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

train_set="train_ml"
train_dev="dev_ml"
test_set="test_ml"
mono_set="mono_ml"

# Change mono_data.sh to data.sh before this

./asr.sh \
    --ngpu 1 \
    --stage 1 \
    --stop_stage 5 \
    --speed_perturb_factors "0.9 1.0 1.1" \
    --lang "ml" \
    --skip_train true \
    --nbpe 150 \
    --asr_exp exp/asr_train_asr_conformer_s3prlfrontend_hubert_fused_raw_ml_bpe150_sp \
    --lm_exp exp/lm_train_lm_ml_bpe150 \
    --feats_type raw \
    --feats_normalize utt_mvn \
    --train_set "${train_set}" \
    --valid_set "${train_dev}" \
    --test_sets "${test_set} ${mono_set}" \
    --lm_train_text "data/${train_set}/text" \
    --bpe_train_text "data/${train_set}/text"


./asr.sh \
    --ngpu 1 \
    --inference_nj 3 \
    --lang "ml" \
    --skip_data_prep true \
    --skip_train true \
    --asr_exp exp/asr_train_asr_conformer_s3prlfrontend_hubert_fused_raw_ml_bpe150_sp \
    --lm_exp exp/lm_train_lm_ml_bpe150 \
    --nbpe 150 \
    --feats_type raw \
    --feats_normalize utt_mvn \
    --train_set "${train_set}" \
    --valid_set "${train_dev}" \
    --test_sets "${mono_set}" \
    --lm_train_text "data/${train_set}/text"

