import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import { Route, BrowserRouter as Router, Switch } from 'react-router-dom';
import App from './App';
import Header from './components/Header';
import Footer from './components/Footer';
import Login from './components/Login'; 
import SignUp from './components/SignUp';
import Logout from './components/Logout';
import Dashboard from './components/Dashboard';

const routing = (
	<Router>
		<React.StrictMode>
			<Header />
			<Switch>
				<Route path='/login' component={Login} exact />
          		<Route path='/signup' component={SignUp} exact />
				<Route path='/logout' component={Logout} exact />
				<Route path='/dashboard' component={Dashboard} exact />
				<Route exact path="/" component={App} />
			</Switch>
			<Footer />
		</React.StrictMode>
	</Router>
);

ReactDOM.render(routing, document.getElementById('root'));