def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso: {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Chevrolet", "Onix", 2020, "ABC-1234")
salvar_carro(marca="Chevrolet", modelo="Onix", ano=2020, placa="ABC-1234")
salvar_carro(**{"marca": "Chevrolet", "modelo": "Onix", "ano": 2020, "placa": "ABC-1234"})