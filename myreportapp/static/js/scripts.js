/*  Formata a numeração do Laudo, Protocolo e Boletim, incluindo o ano do registro.
    Aplica o formato "X.XXX/AAAA".*/
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


// Função para gerar o preâmbulo
function generatePreamble(designatedDate, city, director, reportingExpert, requestingAuthority) {
    // Extrai dia, mês e ano da data
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

// Dá uma aparencia melhor aos nomes digitados pelo usuário, no padrão da língua formal.
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


function beforeThan(priorDate, priorHour, lastDate, lastHour) {
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


function resizeImage(file, width, height, callback) {
    const reader = new FileReader();

    reader.onload = function (event) {
        const img = new Image();
        img.src = event.target.result;

        img.onload = function () {
            const canvas = document.createElement('canvas');
            const ctx = canvas.getContext('2d');

            // Define o tamanho do canvas, considerando a borda de 1px
            canvas.width = width; // +2 para incluir 1px de borda em cada lado
            canvas.height = height; // +2 para a borda de 1px em cada lado

            // Preenche o fundo com a cor da borda (preta)
            ctx.fillStyle = "black";
            ctx.fillRect(0, 0, canvas.width, canvas.height); // Pinta todo o canvas com preto

            // Desenha a imagem redimensionada dentro da borda (1px de distância das bordas)
            ctx.drawImage(img, 1, 1, width - 2, height - 2);

            // Converte o canvas para Base64
            const resizedBase64 = canvas.toDataURL('image/jpeg'); // ou 'image/png'

            // Retorna o Base64 para o callback
            callback(resizedBase64);
            //alert('imagem baixada');
        };
    };

    reader.readAsDataURL(file);
}


function handleImageResize(file, hiddenInputElement) {
    resizeImage(file, 1200, 800, function (resizedBase64) {
        hiddenInputElement.value = resizedBase64;
    });
}


function createMinitagsPDF(text) {
    const { jsPDF } = window.jspdf;
    let pdf = new jsPDF();

    // Definir tamanho e estilo da fonte
    pdf.setFont("Helvetica");  // Fonte negrito
    pdf.setFontSize(12);               // Tamanho da fonte

    // Coordenadas iniciais de X e Y
    let x = 20;
    let y = 20;
    let lineHeight = 10;  // Controla o espaçamento entre as linhas

    // Dividir o texto em linhas e definir espaçamento entre elas
    let lines = text.split("\n");  // Divide o texto por quebras de linha
    lines.forEach(function(line) {
        pdf.text(line, x, y);
        y += lineHeight;  // Incrementa Y para espaçamento entre linhas
    });

    // Salvar o PDF
    pdf.save('minitags.pdf');
}


function teste(texto) {
    alert(texto)
}

