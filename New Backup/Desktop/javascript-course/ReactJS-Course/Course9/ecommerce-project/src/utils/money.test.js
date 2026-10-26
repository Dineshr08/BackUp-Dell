import {it, describe,expect } from 'vitest';
import { formatMoney } from './money';

describe('formatMoney', () => {

  it('check the data working for $1099', () => {
    expect(formatMoney(1099)).toBe('$10.99');
  });
  it('check the data working for $10 & $103', () => {
    expect(formatMoney(10)).toBe('$0.10');
    expect(formatMoney(103)).toBe('$1.03');
  });
});