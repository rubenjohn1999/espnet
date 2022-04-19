inference_file = open("exp/asr_train_asr_conformer_s3prlfrontend_hubert_fused_raw_ml_bpe150_sp/inference_lm_lm_train_lm_ml_bpe150_valid.loss.ave_asr_model_valid.acc.ave/mono_ml/text")
output_file = open("output.tsv", "w")

for line in inference_file:
    values = line[5:]
    result = values.split(" ")
    file_name = result[0]
    text = " ".join(result[1:])
    output_file.write(file_name + "\t" + text)
output_file.close()
inference_file.close()