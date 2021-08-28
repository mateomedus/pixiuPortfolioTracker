import React, { useEffect, useState } from 'react';
import './App.css';
import Dashboard from './components/Dashboard';
import DashboardLoadingComponent from './components/DashboardLoading';

function App() {
	const DashboardLoading = DashboardLoadingComponent(Dashboard);
	const [appState, setAppState] = useState({
		loading: false,
		dashboard: null,
	});

	useEffect(() => {
		setAppState({ loading: true });
		const apiUrl = `http://127.0.0.1:8000/api/`;
		fetch(apiUrl)
			.then((data) => data.json())
			.then((dashboard) => {
				setAppState({ loading: false, dashboard: dashboard });
			});
	}, [setAppState]);
	return (
		<div className="App">
			<DashboardLoading isLoading={appState.loading} dashboard={appState.dashboard} />
		</div>
	);
}
export default App;