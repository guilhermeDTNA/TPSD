import React, {Component} from 'react';
import api from './api';
import {FaSpinner} from 'react-icons/fa';


export default class Home extends Component{

	constructor(props) {
		super(props);
		this.state = {
			campo: '',
			loading: false
		}

		this.buscar = this.buscar.bind(this);
	}

	async buscar(event){
		let state = this.state;
		

		if(this.state.campo === ''){
			
		}
		else{
			let campo = this.state.campo;
			//console.log(campo);
			state.loading = true;
			this.setState(state);

			const resposta = await api.get(campo+'/')
			//.then(function(response){
    //console.log(response.data); // ex.: { user: 'Your User'}
    console.log(resposta); // ex.: 200
    

//});			

		}
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
				<label>Digite o termo de busca:</label><br />
				<input type="text" autoComplete="on" required autoFocus value={this.state.campo} onChange={(e) => this.setState({campo: e.target.value})} placeholder="Ex: Teoria da Computação" /><br />


				<button type="submit">Buscar</button>

				</form>
				</div> 

				</div>
				);
			}
		}
	}