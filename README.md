# Download de Músicas do YouTube com Bot do Telegram

Este é um programa em Python que permite baixar músicas do YouTube e convertê-las em arquivos de áudio MP3 usando o módulo PyTube e MoviePy. Também inclui integração com o bot do Telegram para enviar as músicas baixadas diretamente para o usuário.

## O programa começa importando os módulos necessários:

```
 pip instal -r requerimentos.txt
```
 - pytube para baixar os vídeos do YouTube
 - moviepy para converter os arquivos de vídeo para áudio
 - os para criar a pasta para os arquivos de música
 - telebot para integração com o bot do Telegram
 
Em seguida, é definida uma função sending que envia a música baixada   para o usuário usando o bot do Telegram. Essa função é chamada  posteriormente na função principal do programa.

A função principal é baixayt que recebe um link do YouTube e o ID do chat do Telegram. A função verifica se o link é uma lista de reprodução ou apenas uma música e, em seguida, baixa a música ou todas as músicas da lista. Depois, converte o vídeo para um arquivo de áudio MP3 e o envia ao usuário usando a função sending.

O programa também inclui um handler para lidar com todas as mensagens recebidas no bot do Telegram. Quando uma mensagem contendo um link do YouTube é recebida, a função baixayt é chamada.

O programa inteiro é executado usando o método polling do bot do Telegram.

Por fim, o programa é destinado a fins educacionais e não deve ser usado para violar direitos autorais.

