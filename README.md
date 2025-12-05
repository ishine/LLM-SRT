

## [ACL 2025 Main] Making LLMs Better Many-to-Many Speech-to-Text Translators with Curriculum Learning

**LLM-SRT paper**: [https://arxiv.org/abs/2409.19510](https://arxiv.org/abs/2409.19510); 

**MCAT paper**: [https://arxiv.org/abs/2512.01512v1](https://arxiv.org/abs/2512.01512v1); 

This project is a subproject of [**SLAM-LLM**](https://github.com/X-LANCE/SLAM-LLM).  

✅ **Current Version LLM-SRT (v1.0)**  
- **Supported 15 Languages**: Chinese (zho), English (eng), Japanese (jpn), Korean (kor), German (deu), French (fra), Indonesian (ind), Italian (ita), Dutch (nld), Portuguese (por), Russian (rus), Spanish (spa), Thai (tha), Vietnamese (vie), Cantonese (yue)
- **210 Translation Directions** - Supports all 210 possible translation directions (15×14 language pairs)  

🚀 **MCAT (v2.0)**: Code and Model: [https://github.com/yxduir/m2m-70](https://github.com/yxduir/m2m-70)
- **Supported 70 Languages**: Afrikaans (afr), Amharic (amh), Arabic (ara), Assamese (asm), Azerbaijani (azj), Belarusian (bel), Bengali (ben), Bosnian (bos), Bulgarian (bul), Catalan (cat), Czech (ces), Chinese (cmn), Welsh (cym), Danish (dan), German (deu), Greek (ell), English (eng), Estonian (est), Persian (fas), Finnish (fin), French (fra), Galician (glg), Gujarati (guj), Hebrew (heb), Hindi (hin), Croatian (hrv), Hungarian (hun), Armenian (hye), Indonesian (ind), Icelandic (isl), Italian (ita), Javanese (jav), Japanese (jpn), Kannada (kan), Georgian (kat), Kazakh (kaz), Khmer (khm), Kyrgyz (kir), Korean (kor), Lao (lao), Latvian (lav), Lithuanian (lit), Malayalam (mal), Macedonian (mkd), Malay (msa), Burmese (mya), Dutch (nld), Norwegian (nob), Nepali (npi), Punjabi (pan), Polish (pol), Portuguese (por), Romanian (ron), Russian (rus), Slovak (slk), Slovenian (slv), Spanish (spa), Serbian (srp), Swedish (swe), Swahili (swh), Tamil (tam), Telugu (tel), Tagalog (tgl), Thai (tha), Turkish (tur), Ukrainian (ukr), Urdu (urd), Uzbek (uzb), Vietnamese (vie), Cantonese (yue)
- **4830 Translation Directions** - Supports all 4830 possible translation directions (70×69 language pairs)


## Installation
```
sudo apt-get install python3-setuptools

conda create -n llm-srt python=3.10 -y
conda activate llm-srt

git clone https://github.com/yxduir/LLM-SRT
cd LLM-SRT

pip install -e .
sudo apt install ffmpeg
pip install -r requirements.txt
```

## Download Model 
Encoder | Adapter | LLM 
|---|---|---
[whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) | [q-former+mlp](https://huggingface.co/yxdu/llm-srt) | [Qwen2.5-3B](https://huggingface.co/Qwen/Qwen2.5-3B) 
```
cd models/

git lfs clone https://huggingface.co/yxdu/llm-srt
git lfs clone https://huggingface.co/openai/whisper-large-v3
# for 3B model (support 15 languages)
git lfs clone https://huggingface.co/Qwen/Qwen2.5-3B
cd ..
```

## Infer Demo
This is an automatic inference script for the fleurs dataset from English (eng) to Chinese (zho).
```
bash examples/st_covost2/scripts/infer_hf.sh
```

## Train Dataset
If you want to train your own model, you can download the following datasets.
```
[Common Voice](https://commonvoice.mozilla.org/en/datasets)

[Fleurs](https://huggingface.co/datasets/google/fleurs)
```



## Data preparation
You need to prepare the data jsonl in this format.  
| audio      | source           | prompt                     | gt            |
|------------|------------------|----------------------------|---------------|
| audio_path | `{name}_{src}_{tgt}` | `<\|{src}\|><\|{tgt}\|>`| `transcription{prompt}translation` |
```
{"audio": "eng/test/139.wav", "source": "fleurs_eng_zho", "prompt": "<|eng|><|zho|>", "gt": "They have feet with scales and claws, they lay eggs, and they walk on their two back legs like a T-Rex.<|eng|><|zho|>它们脚上有鳞片和爪子，会产卵，还像霸王龙一样用两条后腿走路。"}
{"audio": "deu/test/0.wav", "source": "fleurs_deu_ara", "prompt": "<|deu|><|ara|>", "gt": "Für die besten Aussichten auf Hongkong sollten Sie die Insel verlassen und zum gegenüberliegenden Ufer von Kowloon fahren.<|deu|><|ara|>لكي تحظى بأفضل المشاهد لهونج كونج، غادر الجزيرة واتجه إلى واجهة كولون البحرية في الجهة المقابلة."}
{"audio": "jpn/test/485.wav", "source": "fleurs_jpn_ita", "prompt": "<|jpn|><|ita|>", "gt": "これらの結晶の組成は、赤外分光法（FTIR）で比較すると、患部のペットの尿中に見られるものと一致します。<|jpn|><|ita|>Al confronto mediante spettroscopia infrarossa (FT-IR), la composizione di questi cristalli corrisponde a quella individuata nell'urina degli animali da compagnia che ne sono colpiti."}
```
## Training and Inference
You can use the following scripts to perform training and inference separately. 
For all.sh, you can modify the training task based on the 'mode' keyword: asr, smt, srt.
```
#train
bash examples/st_covost2/scripts/all.sh


#infer
bash examples/st_covost2/scripts/infer_all.sh
bash examples/st_covost2/scripts/infer_hf.sh
```


##  Citation
```
@article{du2025speech2text,  
  title     = {Making LLMs Better Many-to-Many Speech-to-Text Translators with Curriculum Learning},
  author    = {Du, Yexing and Pan, Youcheng and Ma, Ziyang and Yang, Bo and Yang, Yifang and Deng, Keqi and Chen, Xie and Xiang, Yang and Liu, Ming and Qin, Bing},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025)},
  year      = {2025},
}
@misc{du2025mcatscalingmanytomanyspeechtotext,
      title={MCAT: Scaling Many-to-Many Speech-to-Text Translation with MLLMs to 70 Languages}, 
      author={Yexing Du and Kaiyuan Liu and Youcheng Pan and Bo Yang and Keqi Deng and Xie Chen and Yang Xiang and Ming Liu and Bin Qin and YaoWei Wang},
      year={2025},
      eprint={2512.01512},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2512.01512}, 
}
```