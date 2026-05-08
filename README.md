# SyncWave

Um projetinho simples que fiz para automatizar duas coisas que eu fazia manualmente e achava chato:

1. Extrair áudio de vídeos;
2. Colocar qualquer áudio em um vídeo.

Nada muito complexo, apenas brincando com Python + FFmpeg

---

## O que esse projeto faz?

Atualmente existem dois scripts:

- `extract_audio.py` → extrai o áudio de um vídeo;
- `insert_audio.py` → substitui o áudio original de um vídeo.

---

## Caso queira utilizar meu projeto também, fique a vontade. Eis os passos para tal:

### Baixar a ferramenta open-source `FFmpeg`;

#### No linux:

```bash
sudo apt update
sudo apt install ffmpeg
```

#### No Windows:
1. Baixar pelo site oficial, clique aqui;
2. Adicionar ao path do sistema.

### Colocar o vídeo ou áudio na pasta correspondente e nomear o arquivo de acordo com o que código espera (video.mp4 ou audio.mp3)

Fique a vontade para alterar esses nomes no código (use sua criatividade).

### Agora é só rodar os scripts

#### Extrair áudio do vídeo

```bash
python extract_audio.py
```

#### Colocar um novo áudio em um vídeo

```bash
python insert_audio.py
```