import type { Card, ResponseAPI } from '@/models/index';
import { transformObjectToCamelCase } from '@/helpers';
import httpClient from './httpClient';

const getCardById = async (id: string): Promise<ResponseAPI<Card>> => {
  const response = await httpClient.get(`/cards/${id}`);
  return transformObjectToCamelCase(response.data);
};

export default getCardById;
