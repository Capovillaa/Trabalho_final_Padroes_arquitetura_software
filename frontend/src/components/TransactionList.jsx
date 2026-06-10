import React from 'react';

function TransactionList({ transactions }) {
  if (transactions.length === 0) {
    return (
      <div className="card" style={{ textAlign: 'center', padding: '40px' }}>
        <p style={{ color: 'var(--text-muted)' }}>Você ainda não possui transações registradas.</p>
      </div>
    );
  }

  const sorted = [...transactions].sort((a, b) => new Date(b.date) - new Date(a.date));

  return (
    <div className="card">
      <div className="transaction-list">
        {sorted.map(t => (
          <div className="transaction-item" key={t.id}>
            <div className="t-info">
              <span className="t-title">{t.title}</span>
              <span className="t-meta">{t.category} • {new Date(t.date).toLocaleDateString('pt-BR')}</span>
            </div>
            <div className={`t-amount ${t.type}`}>
              {t.type === 'despesa' ? '- ' : '+ '}
              {new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(t.amount)}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default TransactionList;
