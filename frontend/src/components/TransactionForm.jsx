import React, { useState } from 'react';

function TransactionForm({ onSubmit, onClose }) {
  const [type, setType] = useState('receita');
  const [title, setTitle] = useState('');
  const [amount, setAmount] = useState('');
  const [category, setCategory] = useState('');
  const [date, setDate] = useState(new Date().toISOString().split('T')[0]);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({
      type,
      title,
      amount: parseFloat(amount),
      category,
      date
    });
  };

  return (
    <div>
      <h2 style={{ marginBottom: '20px', fontSize: '20px', fontWeight: 600 }}>Nova Transação</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Tipo</label>
          <select value={type} onChange={(e) => setType(e.target.value)} required>
            <option value="receita">Entrada (Receita)</option>
            <option value="despesa">Saída (Despesa)</option>
          </select>
        </div>

        <div className="form-group">
          <label>Título</label>
          <input 
            type="text" 
            placeholder="Ex: Salário, Aluguel..." 
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label>Categoria</label>
          <input 
            type="text" 
            placeholder="Ex: Alimentação, Lazer..." 
            value={category}
            onChange={(e) => setCategory(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label>Data</label>
          <input 
            type="date" 
            value={date}
            onChange={(e) => setDate(e.target.value)}
            required
          />
        </div>

        <div className="form-group">
          <label>Valor (R$)</label>
          <input 
            type="number" 
            step="0.01"
            min="0.01"
            placeholder="0.00" 
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
          />
        </div>

        <div className="form-actions">
          <button type="button" className="cancel-btn" onClick={onClose}>Cancelar</button>
          <button type="submit" className="submit-btn">Salvar</button>
        </div>
      </form>
    </div>
  );
}

export default TransactionForm;
