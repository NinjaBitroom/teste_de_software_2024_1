let buttonBuscarCep = document.querySelector("#buscaCepButton");
let cepElement = document.getElementById("cep");

function buscarCep(cep) {
    let logradouroInput = document.getElementById("logradouro");
    let bairroInput = document.getElementById("bairro");
    let cidadeInput = document.getElementById("cidade");
    let ufInput = document.getElementById("uf");

    fetch(`https://viacep.com.br/ws/${cep}/json/`)
        .then(data => data.json())
        .then(resposta => {
            console.log(resposta);
            if (resposta.erro) {
                throw new Error("");
            }
            logradouroInput.value = resposta.logradouro;
            bairroInput.value = resposta.bairro;
            cidadeInput.value = resposta.localidade;
            ufInput.value = resposta.uf;

        }).catch(error => {
        console.log(error);
        alert('CEP Inválido')
    });
}


// Abaixo estou mudando o comportamento do input do cep pra aceitar apenas números
cepElement.addEventListener("input", event => {
    event.preventDefault();
    let cpfInput = event.target;
    let textoCpfInput = cpfInput.value.replace(/\D/g, ''); // Mantém apenas os números

    if (textoCpfInput.length > 5) {
        textoCpfInput = textoCpfInput.substring(0, 5) + '-' + textoCpfInput.substring(5);
    } else if (textoCpfInput.length > 0) {
        textoCpfInput = textoCpfInput.substring(0, 5) + (textoCpfInput.length === 5 ? '-' : '');
    }

    // Atualizando o valor do input
    cpfInput.value = textoCpfInput;

    // Verifica se o usuário está apagando e o cursor está após o hífen
    if (event.inputType === "deleteContentBackward" && cpfInput.value.endsWith('-')) {
        cpfInput.value = cpfInput.value.substring(0, cpfInput.value.length - 1);
    }
});


buttonBuscarCep.addEventListener("click", () => buscarCep(cepElement.value));

