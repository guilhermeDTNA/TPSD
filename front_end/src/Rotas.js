import React, {Component} from 'react';
import { BrowserRouter, Switch, Route, Redirect } from 'react-router-dom';

import Home from './Home';
import Nao_Encontrado from './404';

class Rotas extends Component {

	render(){
		return(
			<BrowserRouter>
			 <Switch>
			<Route exact path="/" component={Home} />


			<Route path="*" component={Nao_Encontrado} />

			 </Switch>
			</BrowserRouter>

			);
	}

}

export default Rotas;