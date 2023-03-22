# utilitariosDeTexto

## Sobre o projeto
Utilitário para ajustes em arquivos CSV, feito para ser utilizado nas situações de:
- O padrão de quebra de linha está incorreto, utilize a quebra de linha Unix \n
- Não foi possivel identificar o encoding do arquivo, o unico encoding aceito é UTF-8.

![gitHub_erros_importador](https://user-images.githubusercontent.com/44988166/226747970-407688cb-3e47-4a17-9855-39b255776b70.png)

## Requisitos
- Python 3.10+

## Utilização
1 - Realize o download do projeto em sua máquina local, baixando em seu local de preferencia

Após descompactado ficará desta forma:

## Estrutura de arquivos
    utilitariosDeTexto
    ├── adapterFilesMS.py
    ├── LICENCE
    └── README.md
    
2 - Deposite os arquivos **desejados** na pasta raiz

**Importante: TODOS os arquivos precisam estar em letras maiusculas, incluíndo a extensão**

| ARQUIVOS       |FORMATO                        |
|----------------|-------------------------------|
|Arquivo de beneficiarios|BENEFICIARIOS.CSV|
|Arquivo de carências|CARENCIAS.CSV|
|Arquivo de especialidades|GM_MS_ESPEC.CSV|
|Arquivo de planos|GM_MS_PLANOS.CSV|
|Arquivo de corpo clínico|GM_MS_CORPOCLI.CSV|
|Arquivo de horários|GM_MS_HORARIOS.CSV|
|Arquivo de qualificação|GM_MS_QUALIFICACAO.CSV|
|Arquivo de tipo de rede credenciada|GM_MS_TPREDE.CSV|
|Arquivo de rede credenciada|GM_MS_REDECRED.CSV|
|Arquivo de medicamentos|GM_MS_MEDICAMENTO.CSV|

## Estrutura de arquivos a serem ajustados
    utilitariosDeTexto
    ├── adapterFilesMS.py
    ├── BENEFICIARIOS.CSV
    ├── CARENCIAS.CSV
    ├── GM_MS_ESPEC.CSV
    │── GM_MS_PLANOS.CSV
    │── GM_MS_CORPOCLI.CSV
    │── GM_MS_HORARIOS.CSV
    │── GM_MS_QUALIFICACAO.CSV
    │── GM_MS_MEDICAMENTO.CSV
    │── GM_MS_TPREDE.CSV
    │── GM_MS_REDECRED.CSV
    ├── LICENCE
    └── README.md

3 - Execute o programa adapterFilesMS.py

    $ python %PATH/adapterFilesMS.py
    
4 - Selecione uma das opções para ajustar o problema ( 1 , 2 ou 3)

![image](https://user-images.githubusercontent.com/44988166/226752733-0f474001-bd0e-4fd5-aea3-88da4c31ef62.png)

5 - Os arquivos ficarão dispostos na pasta

    /msConvert

![image](https://user-images.githubusercontent.com/44988166/226753110-c76d8a29-0ca1-4f76-9377-d8921a3b3d24.png)

