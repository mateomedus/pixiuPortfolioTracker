import React, { useState, useEffect } from 'react';
import axiosInstance from '../axios';

import { useHistory } from 'react-router-dom';
//MaterialUI
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';



const useStyles = makeStyles((theme) => ({
	paper: {
		marginTop: theme.spacing(8),
		display: 'flex',
		flexDirection: 'column',
		alignItems: 'center',
	},
	avatar: {
		margin: theme.spacing(1),
		backgroundColor: theme.palette.secondary.main,
	},
	form: {
		width: '100%',
		marginTop: theme.spacing(3),
	},
	submit: {
		margin: theme.spacing(3, 0, 2),
	},
}));

export default function BinanceApi() {
	useEffect(() => {
        if (localStorage.getItem('token') === null) {
          window.location.replace('http://localhost:3000/login');
        }
      }, []);

	const history = useHistory();
	const initialFormData = Object.freeze({
		api_key: '',
		api_secret: '',
	});

	const [formData, updateFormData] = useState(initialFormData);

	const handleChange = (e) => {
		updateFormData({
			...formData,
			// Trimming any whitespace
			[e.target.name]: e.target.value.trim(),
		});
	};

	const handleSubmit = (e) => {
		e.preventDefault();
		console.log(formData);
/*
		axiosInstance
			.post('v1/users/auth/register/', {
				api_key: formData.api_key,
				api_secret: formData.api_secret,
			})
			.then((res) => {
				localStorage.setItem('token', res.data.key);
				axiosInstance.defaults.headers['Authorization'] =
					'Token ' + localStorage.getItem('token');
				history.push('/dashboard');
			});
            */
	};

	const classes = useStyles();

	return (
		<Container component="main" maxWidth="xs">
			<CssBaseline />
			<div className={classes.paper}>
				<Typography component="h1" variant="h5">
					Please provide us with your Binance account Api Key and Api Secret.
				</Typography>
				<form className={classes.form} noValidate>
					<Grid container spacing={2}>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="api_key"
								label="Binance Api Key"
								name="api_key"
								autoComplete="api_key"
								onChange={handleChange}
							/>
						</Grid>
						<Grid item xs={12}>
							<TextField
								variant="outlined"
								required
								fullWidth
								id="api_secret"
								label="Api Secret"
								name="api_secret"
								autoComplete="api_secret"
								onChange={handleChange}
							/>
						</Grid>
					</Grid>
					<Button
						type="submit"
						fullWidth
						variant="contained"
						color="primary"
						className={classes.submit}
						onClick={handleSubmit}
					>
						Confirm
					</Button>
				</form>
			</div>
		</Container>
	);
}