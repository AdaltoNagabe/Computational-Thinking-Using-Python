troca_pneu
Inicio

	//Rotina inicial	
    ParaCarroAcostamento(LocalPlano);
	PuxarFreioDeMao();
	DesligarVeiculo();
    
	//Rotina de seguranca
	LigarPiscaAlerta();
	EngatarMarcha();
		
	//Rotina de preparacao
	AbrirPortaMalas();
	VerificarKitFerramentas(chaveDeRoda, macaco, triangulo);
	VerificarPneuReserva(estepe);
	
	//Decisao
	Se
		((estepe <- furado ou estepe <-0) ou macaco <-0 ou chaveDeRoda <- 0 ou triangulo <-0);
		ChamarGuincho();
	Senao
	
		//Execução da Troca
		RetirarKitFerramentas(chaveDeRoda, macaco, triangulo);
		RetirarPneuReserva(estepe);
		SinalizarVia(triangulo);
		PosicionarPneuReservaProximo(estepe);
		
		Enquanto (parafuso <- 1 ate parafuso <- ultimo) Faça
			AfrouxarParafuso(chaveDeRoda);
		FimEnquanto
    
		PosicionarMacaco();
		LevantarVeiculo(macaco);
		RemoverParafusos(manual);
		
		Enquanto (parafuso <- 1 ate parafuso <- ultimo) Faça
			RetirarTodosParafusos(manual);
		FimEnquanto

		RetirarPneu(pneuFurado);
		ColocarNovoPneu(estepe);
		
		Enquanto (parafuso <- 1 ate parafuso <- ultimo) Faça
			ColocarParafusos(manual);;
		FimEnquanto
			
        AbaixarVeiculo(macaco);
												
		Enquanto (parafuso <- 1 ate parafuso <- ultimo) Faça
			ApertarParafuso(chaveDeRoda);
		FimEnquanto
    
		GuardarPneu(pneuFurado);
		GuardarKitFerramentas(macaco, chaveDeRoda, triangulo);
        FecharPortaMalas();
		SeguirViagem();

Fim