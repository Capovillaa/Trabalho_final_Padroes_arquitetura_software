import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { LayoutDashboard, Receipt, PlusCircle, Wallet } from 'lucide-react';
import Dashboard from './components/Dashboard';
import TransactionList from './components/TransactionList';
import TransactionForm from './components/TransactionForm';

const API_URL = 'http://127.0.0.1:8000/api/v1';

function App() {
  const [transactions, setTransactions] = useState([]);
  const [balance, setBalance] = useState(0);
  const [activeTab, setActiveTab] = useState('dashboard');
  const [isFormOpen, setIsFormOpen] = useState(false);

  const fetchData = async () => {
    try {
      const [transRes, balRes] = await Promise.all([
        axios.get(`${API_URL}/transactions`),
        axios.get(`${API_URL}/balance`)
      ]);
      setTransactions(transRes.data);
      setBalance(balRes.data.balance);
    } catch (error) {
      console.error("Erro ao buscar dados", error);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleAddTransaction = async (data) => {
    try {
      await axios.post(`${API_URL}/transactions`, data);
      await fetchData();
      setIsFormOpen(false);
    } catch (error) {
      console.error("Erro ao criar transação", error);
      alert("Erro ao criar transação");
    }
  };

  return (
    <div className="app-container">
      <aside className="sidebar">
        <div className="logo">
          <Wallet size={28} className="logo-icon" />
          <h1>FinanceLite</h1>
        </div>
        
        <nav className="nav-menu">
          <button 
            className={`nav-item ${activeTab === 'dashboard' ? 'active' : ''}`}
            onClick={() => setActiveTab('dashboard')}
          >
            <LayoutDashboard size={20} />
            Dashboard
          </button>
          <button 
            className={`nav-item ${activeTab === 'transactions' ? 'active' : ''}`}
            onClick={() => setActiveTab('transactions')}
          >
            <Receipt size={20} />
            Transações
          </button>
        </nav>
      </aside>

      <main className="main-content">
        <header className="top-header">
          <h2>{activeTab === 'dashboard' ? 'Visão Geral' : 'Suas Transações'}</h2>
          <button className="primary-btn" onClick={() => setIsFormOpen(true)}>
            <PlusCircle size={20} />
            Nova Transação
          </button>
        </header>

        <div className="content-area">
          {activeTab === 'dashboard' ? (
            <Dashboard transactions={transactions} balance={balance} />
          ) : (
            <TransactionList transactions={transactions} />
          )}
        </div>
      </main>

      {isFormOpen && (
        <div className="modal-overlay" onClick={() => setIsFormOpen(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <TransactionForm onSubmit={handleAddTransaction} onClose={() => setIsFormOpen(false)} />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
