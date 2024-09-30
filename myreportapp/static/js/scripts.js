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


/*  COMPARA DUAS DATAS ACOMPANHADAS DE SUAS RESPECTIVAS HORAS E VERIFICA SE UMA É MENOR OU NÃO
    RETORNA UM BOOLEANO */
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

function teste(texto) {
    alert(texto);
}