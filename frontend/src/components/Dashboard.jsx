import React from 'react';
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer, BarChart, Bar, XAxis, YAxis, CartesianGrid } from 'recharts';

const COLORS = ['#0071e3', '#34c759', '#ff3b30', '#ff9f0a', '#af52de', '#5856d6'];

function Dashboard({ transactions, balance }) {
  const expenses = transactions.filter(t => t.type === 'despesa');
  const incomes = transactions.filter(t => t.type === 'receita');

  const totalExpenses = expenses.reduce((acc, t) => acc + t.amount, 0);
  const totalIncomes = incomes.reduce((acc, t) => acc + t.amount, 0);

  const expensesByCategory = expenses.reduce((acc, t) => {
    acc[t.category] = (acc[t.category] || 0) + t.amount;
    return acc;
  }, {});

  const pieData = Object.keys(expensesByCategory).map(key => ({
    name: key,
    value: expensesByCategory[key]
  }));

  const barData = [
    { name: 'Receitas', valor: totalIncomes },
    { name: 'Despesas', valor: totalExpenses }
  ];

  return (
    <div className="dashboard">
      <div className="dashboard-grid">
        <div className="card stat-card balance-card">
          <div className="label">Saldo Disponível</div>
          <div className="value">
            {new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(balance)}
          </div>
        </div>

        <div className="card stat-card">
          <div className="label">Total de Entradas</div>
          <div className="value success">
            {new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(totalIncomes)}
          </div>
        </div>

        <div className="card stat-card">
          <div className="label">Total de Saídas</div>
          <div className="value danger">
            {new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(totalExpenses)}
          </div>
        </div>
      </div>

      <div className="charts-grid">
        <div className="card">
          <h3 style={{ marginBottom: '20px', fontSize: '16px', color: 'var(--text-muted)' }}>Despesas por Categoria</h3>
          {pieData.length > 0 ? (
            <div style={{ height: 300 }}>
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={pieData}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={100}
                    paddingAngle={5}
                    dataKey="value"
                  >
                    {pieData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    ))}
                  </Pie>
                  <Tooltip formatter={(value) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value)} />
                </PieChart>
              </ResponsiveContainer>
            </div>
          ) : (
            <div style={{ textAlign: 'center', color: 'var(--text-muted)', marginTop: '40px' }}>Sem dados de despesas</div>
          )}
        </div>

        <div className="card">
          <h3 style={{ marginBottom: '20px', fontSize: '16px', color: 'var(--text-muted)' }}>Receitas vs Despesas</h3>
          <div style={{ height: 300 }}>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={barData} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--border-color)" />
                <XAxis dataKey="name" tick={{ fontSize: 12 }} axisLine={false} tickLine={false} />
                <YAxis hide />
                <Tooltip cursor={{ fill: 'transparent' }} formatter={(value) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(value)} />
                <Bar dataKey="valor" radius={[4, 4, 0, 0]}>
                  {barData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={entry.name === 'Receitas' ? 'var(--success)' : 'var(--danger)'} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;
