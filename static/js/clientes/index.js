let listaRemoveButton = document.querySelectorAll(".removerCliente");

listaRemoveButton.forEach(item => {
    item.addEventListener("click", () => {
        let formulario = item.closest(".delete_cliente_form");

        if (formulario && confirm("Tem certeza que deseja excluir esse cliente?")) {
            formulario.submit();
        }
    })
})