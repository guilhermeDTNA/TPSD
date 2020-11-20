import React, {Component} from 'react';
import api from './api';
import {FaSpinner} from 'react-icons/fa';
import 'bootstrap/dist/css/bootstrap.css';
import './App.css';


export default class Home extends Component{

	constructor(props) {
		super(props);
		this.state = {
			catalogo: '',
			entrada: '',
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
		this.alteraAgregacao = this.alteraAgregacao.bind(this);
		this.alteraEstrutura = this.alteraEstrutura.bind(this);
	}

	async buscar(event){
		let state = this.state;
		
		let catalogo = this.state.catalogo;
		let entrada = this.state.entrada;
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

		state.loading = true;
		this.setState(state);


		let url = 'catalogo='+catalogo+'&entrada='+entrada+'&titulo='+titulo+'&idioma='+idioma+'&descricao='+descricao+'&palavras_chaves='+palavras_chave+'&cobertura='+cobertura+'&estrutura='+estrutura+'&nivel_agregacao='+agregacao+'&formato='+formato+'&data='+data+'&tamanho='+tamanho;

			//Retira acentos e letras maiúsculas
			//url = url.normalize("NFD");
			url = url.toLowerCase();


			const resposta = await api.get(url);



    //Verifica tamanho do array de objetos
    if(resposta.data.length === 0){
    	alert('Sua pesquisa não retornou resultado!');
    }
    else{
    	//alert(agregacao);
    let pagina = window.open('http://localhost:8000/consulta_objetos?&format=json&'+url,"_blank"); // abre em nova janela
}


//});			


state.loading = false;


state.catalogo = '';
state.entrada = '';
state.titulo = '';
state.idioma = '';
state.descricao = '';
state.palavras_chave = '';
state.cobertura = '';
state.estrutura = '';
state.agregacao = '';
state.formato = '';
state.data = '';
state.tamanho = '';


this.setState(state);
		//Não atualiza a página
		//event.preventDefault();
	}

	alteraAgregacao(event) {
		
		//if(event.target.value==='2' || event.target.value==='3' || event.target.value==='4'){
			this.setState({agregacao: event.target.value});
		//} else {
		//	this.setState({agregacao: '1'});
		//}
	}

	alteraEstrutura(event) {
		
		//if(event.target.value==='Coleção' || event.target.value==='Rede' || event.target.value==='Hierarquia' || event.target.value==='Linear'){
			this.setState({estrutura: event.target.value});
		//} else {
		//	this.setState({estrutura: 'Atômico'});
		//}
	}
	


	//<input type="number" autoComplete="on" autoFocus value={this.state.agregacao} onChange={(e) => this.setState({agregacao: e.target.value})} placeholder="1, 2, 3 ou 4" /></td>
	//<input type="text" autoComplete="on" autoFocus value={this.state.estrutura} onChange={(e) => this.setState({estrutura: e.target.value})} placeholder="Atômico, coleção, rede, hierarquia ou linear" /></td>


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

				<div className="container-1">

				<div className="topo">
				<div className="titulo">Pesquisar Objetos de Aprendizagem</div>
				</div>

				<div className="corpo">
				<form onSubmit={this.buscar} id="campo">
				<label>Digite o(s) termo(s) de busca:</label><br />


				<div className="table-responsive-lg">
				<table className="formulario">
				<tr>

				<td className="coluna">Catálogo: <input type="text" autoComplete="on" autoFocus value={this.state.catalogo} onChange={(e) => this.setState({catalogo: e.target.value})} placeholder="Ex: OBJ-1" /></td>
				<td className="coluna">Entrada: <input type="text" autoComplete="on" autoFocus value={this.state.entrada} onChange={(e) => this.setState({entrada: e.target.value})} placeholder="Ex: www.google.com" /></td>
				<td className="coluna">Título: <input type="text" autoComplete="on" autoFocus value={this.state.titulo} onChange={(e) => this.setState({titulo: e.target.value})} placeholder="Ex: Teoria da Computação" /></td>

				</tr>

				<tr>

				<td className="coluna">Idioma: <input type="text" autoComplete="on" autoFocus value={this.state.idioma} onChange={(e) => this.setState({idioma: e.target.value})} placeholder="Ex: Português" /></td>
				<td className="coluna">Descrição: <input type="text" autoComplete="on" autoFocus value={this.state.descricao} onChange={(e) => this.setState({descricao: e.target.value})} placeholder="Ex: Artigo que introduz fundamentos" /></td>
				<td className="coluna">Palavras-chave: <input type="text" autoComplete="on" autoFocus value={this.state.palavras_chave} onChange={(e) => this.setState({palavras_chave: e.target.value})} placeholder="Ex: Teoria da Computação, Inteligência Artificial" /></td>

				</tr>

				<tr>

				<td className="coluna">Cobertura: <input type="text" autoComplete="on" autoFocus value={this.state.cobertura} onChange={(e) => this.setState({cobertura: e.target.value})} placeholder="Ex: Diamantina, 2020" /></td>
				<td className="coluna">Estrutura: 

				<p align="center" >
				<select className="select" onChange={this.alteraEstrutura}>
				<option>Selecionar</option>
				<option value='Atômico'>Atômico</option>
				<option value='Coleção'>Coleção</option>
				<option value='Rede'>Rede</option>
				<option value='Hierarquia'>Hierarquia</option>
				<option value='Linear'>Linear</option>
				</select>
				</p>
				</td>

				<td className="coluna">Nível de agregação: 

				<p align="center" >
				<select className="select" onChange={this.alteraAgregacao}>
				<option>Selecionar</option>
				<option value='1'>1</option>
				<option value='2'>2</option>
				<option value='3'>3</option>
				<option value='4'>4</option>
				</select>
				</p>
				</td>		

				</tr>

				<tr>

				<td className="coluna">Formato: <input type="text" autoComplete="on" autoFocus value={this.state.formato} onChange={(e) => this.setState({formato: e.target.value})} placeholder="Ex: PDF, JPG, XML" /></td>
				<td className="coluna">Data: <input type="date" autoComplete="on" autoFocus value={this.state.data} onChange={(e) => this.setState({data: e.target.value})} /></td>
				<td className="coluna">Tamanho (bytes): <input type="number" autoComplete="on" autoFocus value={this.state.tamanho} onChange={(e) => this.setState({tamanho: e.target.value})} placeholder="Ex: 1024" /></td>

				</tr>

				<tr>
				<td></td>
				<td align="center"><button type="submit">Buscar</button></td>
				<td></td>
				</tr>
				</table>
				</div>

				
				</form>
				</div> 

				</div>
				);
		}
	}
}