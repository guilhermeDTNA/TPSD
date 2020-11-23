import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import './App.css';
import imagem from './img/404.png'

class Error extends Component{
	render(){
		return(

			<div className="conteudo-404">
			<br /><br /><br /><br />
			<h2>Página não encontrada</h2>
				<Link to="/">Voltar para a página inicial</Link><br />

				<img src={imagem} className="img" />
			</div>

			);
	}
	
}

export default Error;