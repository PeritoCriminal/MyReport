function formatStringWithYear(str, date) {
    /*
    Formata a numeração do Laudo, Protocolo e Boletim, incluindo o ano do registro.
    Aplica o formato "X.XXX/AAAA".
    */

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

function toNiceName(nomeDeAlguem) {

    // Lista de preposições que devem permanecer em minúsculas quando não estiverem no início ou no fim do nome
    const preposicoes = new Set(['de', 'da', 'do', 'dos', 'das', 'e', 'ou', 'para', 'com', 'em', 'a', 'o', 'do', 'dos']);

    // Divide o nome em palavras
    const palavras = nomeDeAlguem.split(/\s+/);

    // Converte as palavras de acordo com as regras
    const palavrasFormatadas = palavras.map((palavra, index) => {
        // Converte a palavra para minúscula
        const palavraFormatada = palavra.toLowerCase();

        // Se a palavra é uma preposição e não está no início ou no fim do nome, mantém em minúsculas
        if (preposicoes.has(palavraFormatada) && index !== 0 && index !== palavras.length - 1) {
            return palavraFormatada;
        } else {
            // Caso contrário, capitaliza a primeira letra
            return palavraFormatada.charAt(0).toUpperCase() + palavraFormatada.slice(1);
        }
    });

    // Junta as palavras formatadas em uma string
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

function handleImageResize(file) {
    resizeImage(file, 1200, 800, function(resizedBase64) {
        // Armazena a string Base64 no input hidden
        document.getElementById('imageGeneralBase64').value = resizedBase64;
    });
}


function resizeImage(file, maxWidth, maxHeight, callback) {
    const reader = new FileReader();
    reader.onload = function(event) {
        const img = new Image();
        img.onload = function() {
            // Calcula o novo tamanho da imagem
            const ratio = Math.min(maxWidth / img.width, maxHeight / img.height);
            const width = img.width * ratio;
            const height = img.height * ratio;

            // Cria um canvas para redimensionar a imagem
            const canvas = document.createElement('canvas');
            canvas.width = width;
            canvas.height = height;

            const ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0, width, height);

            // Converte o canvas para Base64
            const resizedBase64 = canvas.toDataURL('image/jpeg', 0.95);  // Ajusta a qualidade para 95%
            callback(resizedBase64);  // Retorna a imagem redimensionada como Base64
        };
        img.src = event.target.result;
    };
    reader.readAsDataURL(file);
}




function teste(texto) {
    alert(texto)
}

