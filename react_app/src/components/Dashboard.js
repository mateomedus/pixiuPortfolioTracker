import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';

const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
    },
    paper: {
      padding: theme.spacing(1),
      textAlign: 'center',
      color: theme.palette.text.secondary,
    },
}));

export default function NestedGrid() {
    const classes = useStyles();

const Dashboard = (props) => {
	const { dashboard } = props;
	const classes = useStyles();
	if (!dashboard || dashboard.length === 0) return <p>Can not find any posts, sorry</p>;
	return (
		<React.Fragment>
			<Container maxWidth="md" component="main">
				<Grid container spacing={5} alignItems="flex-end">
					{dashboard.map((coin) => {
						return (
							// Enterprise card is full width at sm breakpoint
							<Grid item key={coin.id} xs={12} >
								<Paper className={classes.card}>
                                    <Typography
											variant="h6"
											component="h2"
											className={classes.postText}
										>
											{coin.name.substr(0, 50)}
									</Typography>
								</Paper>
                                <Paper className={classes.card}>
                                    <Typography
											variant="h6"
											component="h2"
											className={classes.postText}
										>
											{coin.price.substr(0, 50)}
									</Typography>
								</Paper>
							</Grid>
						);
					})}
				</Grid>
			</Container>
		</React.Fragment>
	);
};
export default Dashboard;