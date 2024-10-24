/*  

MYREPORT é um projeto independente.
Oferece um ambiente para edição de laudos periciais,
voltado especialmente para Peritos Criminais Oficiais do Estado de São Paulo.
Idealizado e inicialmente desenvolvido pelo Perito Criminal Marcos de Oliveira Capristo.
Contato: marcos.moc@policiacientifica.sp.gov.br | (19) 9 8231-2774
    
*/

/*  

    ESSE MÓUDULO CONTEM FUNÇÕES js COMUNS A TODOS OS MÓDULOS DESSA APLICAÇÃO 
    OUTRAS FUNÇÕES ESPECIFICAS DE CADA APLICAÇÃO ESTÃO NO PRÓPRIO TEMPLATE DA APLICAÇÃO.
    
*/


/*  FORMATA O NUMERO DO LAUDO, DO RE, DO BOLETIM COM UMA BARRA OBLIQUA E O ANO. */
function formatStringWithYear(str, date) {
    if (str.includes('/')) {
        return str.toUpperCase();
    }
    let _date;
    if (date instanceof Date) {
        _date = new Date(date);
    } else {
        _date = new Date();
    }
    let _str;
    try {
        const number = parseInt(str, 10);
        if (!isNaN(number)) {
            _str = number.toLocaleString('pt-BR').trim().toUpperCase();
        } else {
            throw new Error("Invalid number");
        }
    } catch (e) {
        _str = str.trim().toUpperCase();
    }
    const year = _date.getFullYear();
    return `${_str}/${year}`;
}


/*  O PREÂMBULO É GERADO DO LADO DO SERVIDOR, COMO MÉTODO DE CLASSE, 
    MAS ESSA FUÇÃO ESTARÁ AQUI DE QAP POR ENQUANTO. */
function generatePreamble(designatedDate, city, director, reportingExpert, requestingAuthority) {
    const dateObj = new Date(designatedDate);
    const day = String(dateObj.getDate()).padStart(2, '0');  // Adiciona o '0' à esquerda se necessário
    const month = String(dateObj.getMonth() + 1).padStart(2, '0');  // Meses são base 0, então soma-se 1
    const year = dateObj.getFullYear();
    const designatedDateFormatted = `${day}-${month}-${year}`;

    let diretorTexto;
    if (director.startsWith('Dr. ')) {
        diretorTexto = `pelo Diretor deste Instituto de Criminalística, o Perito Criminal ${director}`;
    } else if (director.startsWith('Dra. ')) {
        diretorTexto = `pela Diretora deste Instituto de Criminalística, a Perita Criminal ${director}`;
    } else {
        diretorTexto = `pelo(a) Diretor(a) deste Instituto de Criminalística, o(a) Perito(a) Criminal ${director}`; // Padrão para outros casos
    }

    let peritoTexto;
    if (reportingExpert.startsWith('Dr. ')) {
        peritoTexto = `o perito criminal ${reportingExpert}`;
    } else if (reportingExpert.startsWith('Dra. ')) {
        peritoTexto = `a perita criminal ${reportingExpert}`;
    } else {
        peritoTexto = `o(a) perito(a) criminal ${reportingExpert}`; // Padrão para outros casos
    }

    let autoridadeTexto;
    if (requestingAuthority.startsWith('Dr. ')) {
        autoridadeTexto = `o Delegado de Polícia ${requestingAuthority}`;
    } else if (requestingAuthority.startsWith('Dra. ')) {
        autoridadeTexto = `a Delegada de Polícia ${requestingAuthority}`;
    } else {
        autoridadeTexto = `o(a) Delegado(a) de Polícia ${requestingAuthority}`; // Padrão para outros casos
    }

    const preamble = `Em ${designatedDateFormatted}, na cidade de ${city} e no Instituto de Criminalística, 
    da Superintendência da Polícia Técnico-Científica, da Secretaria de Segurança Pública do Estado de São Paulo, 
    ${diretorTexto}, foi designado ${peritoTexto} para proceder ao Exame Pericial especificado em requisição de exame assinada pela Autoridade Policial, 
    ${autoridadeTexto}.`;

    return preamble;
}


/*  DA UMA MELHORADA NO NOME DIGIADO PELO USUÁRIO, 
    ACOMAPNHANDO O FORMATO OFICIAL DA LÍNGUA PORTUGUESA COM RELAÇÃO ÀS PREPOSIÇÕES */
function toNiceName(nomeDeAlguem) {
    const preposicoes = new Set(['de', 'da', 'do', 'dos', 'das', 'e', 'ou', 'para', 'com', 'em', 'a', 'o', 'do', 'dos']);
    const palavras = nomeDeAlguem.split(/\s+/);
    const palavrasFormatadas = palavras.map((palavra, index) => {
        const palavraFormatada = palavra.toLowerCase();
        if (preposicoes.has(palavraFormatada) && index !== 0 && index !== palavras.length - 1) {
            return palavraFormatada;
        } else {
            return palavraFormatada.charAt(0).toUpperCase() + palavraFormatada.slice(1);
        }
    });
    return palavrasFormatadas.join(' ');
}


/*  VERIFICA SE UMA DATA É VÁLIDA */
function isValidDate(dateString) {
    try {
        const date = new Date(dateString);
        if (isNaN(date.getTime())) {
            throw new Error('Data inválida');
        }
        return true;
    } catch (error) {
        console.error(error.message);
        return false;
    }
}

/*  VERIFICA SE UMA HORA É VÁLIDA */
function isValidTime(timeString) {
    try {
        const timePattern = /^([0-1]\d|2[0-3]):([0-5]\d)$/;        
        if (!timeString.match(timePattern)) {
            throw new Error('Hora inválida');
        }
        return true;
    } catch (error) {
        console.error(error.message);
        return false;
    }
}


/*  COMPARA DUAS DATAS ACOMPANHADAS DE SUAS RESPECTIVAS HORAS E VERIFICA SE UMA É MENOR OU NÃO
    RETORNA UM BOOLEANO */
function beforeThan(priorDate, priorHour, lastDate, lastHour) {
    if (!(priorDate instanceof Date)){
        priorDate = new Date(priorDate);
    }
    if (!(priorHour instanceof Date)) {
        priorHour = new Date(`1970-01-01T${priorHour}:00`);
    }
    if (!(lastDate instanceof Date)) {
        lastDate = new Date(lastDate);
    }
    if (!(lastHour instanceof Date)) {
        lastHour = new Date(`1970-01-01T${lastHour}:00`);
    }
    let beforeDateTime = new Date(
        priorDate.getFullYear(),
        priorDate.getMonth(),
        priorDate.getDate(),
        priorHour.getHours(),
        priorHour.getMinutes()
    );

    let lastDateTime = new Date(
        lastDate.getFullYear(),
        lastDate.getMonth(),
        lastDate.getDate(),
        lastHour.getHours(),
        lastHour.getMinutes()
    );
    return beforeDateTime < lastDateTime;
}


/*  REDIMENSIONA UMA IMAGEM, CRIA BORDA E SALVA COMO TXT BASE 64
    O TXT SERÁ É NO BD E, QUANDO NECESSÁRIO A IMAGEM SERÁ RECUPERADA */
function resizeImage(file, width, height, callback) {
    const reader = new FileReader();

    reader.onload = function (event) {
        const img = new Image();
        img.src = event.target.result;

        img.onload = function () {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');

            canvas.width = width;
            canvas.height = height;

            ctx.fillStyle = "black";
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            ctx.drawImage(img, 1, 1, width - 2, height - 2);

            const resizedBase64 = canvas.toDataURL('image/jpeg');
            callback(resizedBase64);
        };
    };
    reader.readAsDataURL(file);
}


function resizeImageForA4(file, callback) {
    const reader = new FileReader();

    reader.onload = function (event) {
        const img = new Image();
        img.src = event.target.result;

        img.onload = function () {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');

            // Definindo dimensões máximas para A4
            const maxWidth = 1240;  // Largura máxima
            const maxHeight = 1754; // Altura máxima

            let width = img.width;
            let height = img.height;

            // Calculando a nova largura e altura mantendo a proporção
            if (width > height) {
                // Imagem mais larga que alta
                if (width > maxWidth) {
                    height *= maxWidth / width;
                    width = maxWidth;
                }
            } else {
                // Imagem mais alta que larga
                if (height > maxHeight) {
                    width *= maxHeight / height;
                    height = maxHeight;
                }
            }

            // Define o tamanho do canvas
            canvas.width = width;
            canvas.height = height;

            // Preenche o fundo com cor preta
            ctx.fillStyle = "black";
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Desenha a imagem redimensionada mantendo a proporção
            ctx.drawImage(img, 1, 1, width - 2, height - 2);

            // Converte o canvas em um arquivo Blob (formato JPEG)
            canvas.toBlob(function (blob) {
                // Cria um novo arquivo de imagem para envio ao servidor
                const resizedImageFile = new File([blob], file.name, {
                    type: 'image/jpeg',
                    lastModified: Date.now()
                });

                // Chama o callback passando o arquivo redimensionado
                callback(resizedImageFile);
            }, 'image/jpeg', 0.9); // Qualidade 90%
        };
    };

    // Lê o arquivo original
    reader.readAsDataURL(file);
}



/*  CHAMA A FUNÇÃO ACIMA, SETANDO OS VALORES DE LARGURA E ALTURA.
    O ELEMENTO INPUT HTML OCULTO RECEBE O TXT BASE 64 QUE É ENVIADO AO BD */
function handleImageResize(file, hiddenInputElement) {
    resizeImage(file, 1200, 800, function (resizedBase64) {
        hiddenInputElement.value = resizedBase64;
    });
}


/*  CRIA ETIQUETAS QUE PODEM SER IMPRESSAS E FIXADAS NAS EMBALAGENS DE AMOSTRAS PARA CONTRRAPERÍCIA */
function createMinitagsPDF(text) {
    const { jsPDF } = window.jspdf;
    let pdf = new jsPDF();

    pdf.setFont("Helvetica");
    pdf.setFontSize(10);

    let x = 20;
    let y = 20;

    const lineHeight = 6;
    const pageHeight = pdf.internal.pageSize.height;

    let lines = text.split("\n");

    lines.forEach(function (line) {
        if (y + lineHeight > pageHeight - 26) {
            pdf.addPage();
            y = 20;
        }
        pdf.text(line, x, y);
        y += lineHeight;
    });
    pdf.save('minitags.pdf');
}

function twoBolleans(bol1, bol2){
    let val = 0;
    if(bol1 && !bol2){
        val = 1;
    }else if(bol1 && bol2){
        val = 2;
    }else if(!bol1 && bol2){
        val = 3;
    }else{
        val = 0;
    }
    return val;
}


function updateFileName() {
    var fileInput = document.getElementById('image');
    var fileLabel = document.getElementById('file-label');
    
    // Define o texto padrão como um "placeholder"
    var defaultText = 'Clique para inserir uma imagem';
    
    // Se um arquivo for selecionado, exibe o nome do arquivo; caso contrário, exibe o texto padrão
    var fileName = fileInput.files.length ? fileInput.files[0].name : defaultText;
    
    fileLabel.textContent = fileName;
}

function teste(texto) {
    alert(texto);
}