export interface Set {
  id: number;
  name: string;
  series: string;
  total: number;
  ptcgoCode: string;
  releaseDate: string;
  updatedAt: string;
  symbolUrl: string;
  logoUrl: string;
  cards?: Card[];
}

export interface Card {
  id: number;
  name: string;
  supertype: string;
  subtypes: string[];
  types: string[];
  setId: string;
  number: string;
  rarity: string;
  images?: Image[];
  market?: Market[];
  set?: Set;
}

export interface Image {
  id: number;
  cardId: number;
  url: string;
  type: string;
}

export interface Market {
  id: number;
  cardId: number;
  url: string;
  updatedAt: string;
  market: string;
}

type DataResponse<T> = T;

export interface ResponseAPI<T> {
  results: DataResponse<T>;
}

export interface ResponseAPIError {
  error_code: string;
  error_message: string;
}
