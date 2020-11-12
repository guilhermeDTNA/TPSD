import React, {Component} from 'react';
import api from './api';
import {FaSpinner} from 'react-icons/fa';


export default class Home extends Component{

	constructor(props) {
		super(props);
		this.state = {
			titulo: '',
			idioma: '',
			descricao: '',
			palavras_chave: '',
			cobertura: '',
			estrutura: '',
			agregacao: '',
			formato: '',
			data: '',
			tamanho: '',
			loading: false
		}

		this.buscar = this.buscar.bind(this);
	}

	async buscar(event){
		let state = this.state;
		
		let titulo = this.state.titulo;
		let idioma = this.state.idioma;
		let descricao = this.state.descricao;
		let palavras_chave = this.state.palavras_chave;
		let cobertura = this.state.cobertura;
		let estrutura = this.state.estrutura;
		let agregacao = this.state.agregacao;
		let formato = this.state.formato;
		let data = this.state.data;
		let tamanho = this.state.tamanho;

			//console.log(campo);
			state.loading = true;
			this.setState(state);


			let url = 'titulo='+titulo+'&idioma='+idioma+'&descricao='+descricao+'&Palavras_chave='+palavras_chave+'&cobertura='+cobertura+'&estrutura='+estrutura+'&agregacao='+agregacao+'&formato='+formato+'&data='+data+'&tamanho='+tamanho;

			//Retira acentos e letras maiúsculas
			url = url.normalize("NFD");
			url = url.toLowerCase();

			console.log('URL: '+url);

			const resposta = await api.get(url+'/')
			//.then(function(response){
    //console.log(response.data); // ex.: { user: 'Your User'}
    console.log(resposta); // ex.: 200
    

//});			


state.loading = false;
state.campo = '';
this.setState(state);
		//Não atualiza a página
		//event.preventDefault();
	}

	render(){
		if(this.state.loading){
			return(
				<div className="conteudo-404">
				<br /><br />
				<h1>Carregando...</h1>
				<FaSpinner color="#FF0000" size={50} className="icon-spin" />
				</div>	
				);
		}
		else {
			return (

				<div className="container">

				<div className="topo">
				<div className="titulo">Pesquisar Objetos de Aprendizagem</div>
				</div>

				<div className="corpo">
				<form onSubmit={this.buscar} id="campo">
				<label>Digite o(s) termo(s) de busca:</label><br />

				<div className="formulario">
				
				<div className="linha" >
				<div className="coluna">Título: <input type="text" autoComplete="on" autoFocus value={this.state.titulo} onChange={(e) => this.setState({titulo: e.target.value})} placeholder="Ex: Teoria da Computação" /></div>

				<div className="coluna">Idioma: <input type="text" autoComplete="on" autoFocus value={this.state.idioma} onChange={(e) => this.setState({idioma: e.target.value})} placeholder="Ex: Português" /></div>
				</div>

				<div className="linha" >
				<div className="coluna">Descrição: <input type="text" autoComplete="on" autoFocus value={this.state.descricao} onChange={(e) => this.setState({descricao: e.target.value})} placeholder="Ex: Artigo que introduz fundamentos" /></div>

				<div className="coluna">Palavras-chave: <input type="text" autoComplete="on" autoFocus value={this.state.palavras_chave} onChange={(e) => this.setState({palavras_chave: e.target.value})} placeholder="Ex: Teoria da Computação, Inteligência Artificial" /></div>
				</div>

				<div className="linha" >
				<div className="coluna">Cobertura: <input type="text" autoComplete="on" autoFocus value={this.state.cobertura} onChange={(e) => this.setState({cobertura: e.target.value})} placeholder="Ex: Diamantina, 2020" /></div>

				<div className="coluna">Estrutura: <input type="text" autoComplete="on" autoFocus value={this.state.estrutura} onChange={(e) => this.setState({estrutura: e.target.value})} placeholder="Atômico, coleção, rede, hierarquia ou linear" /></div>
				</div>

				<div className="linha" >
				<div className="coluna">Nível de agregação: <input type="number" autoComplete="on" autoFocus value={this.state.agregacao} onChange={(e) => this.setState({agregacao: e.target.value})} placeholder="1, 2, 3 ou 4" /></div>

				<div className="coluna">Formato: <input type="text" autoComplete="on" autoFocus value={this.state.formato} onChange={(e) => this.setState({formato: e.target.value})} placeholder="Ex: PDF, JPG, XML" /></div>
				</div>

				<div className="linha" >
				<div className="coluna">Data: <input type="date" autoComplete="on" autoFocus value={this.state.data} onChange={(e) => this.setState({data: e.target.value})} /></div>

				<div className="coluna">Tamanho (bytes): <input type="number" autoComplete="on" autoFocus value={this.state.tamanho} onChange={(e) => this.setState({tamanho: e.target.value})} placeholder="Ex: 1024" /></div>
				</div>
				</div>

				<div className="linha">
				<button type="submit">Buscar</button>
				</div>
				</form>
				</div> 

				</div>
				);
		}
	}
}