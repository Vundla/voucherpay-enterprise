import { DataSource } from 'typeorm';
import { config } from '../config';

export const AppDataSource = new DataSource({
  type: 'mysql',
  host: config.DB_HOST,
  port: config.DB_PORT,
  username: config.DB_USERNAME,
  password: config.DB_PASSWORD,
  database: config.DB_NAME,
  synchronize: config.NODE_ENV === 'development',
  logging: config.NODE_ENV === 'development',
  entities: [__dirname + '/../models/*.{ts,js}'],
  migrations: [__dirname + '/migrations/*.{ts,js}'],
  subscribers: [__dirname + '/subscribers/*.{ts,js}'],
  charset: 'utf8mb4',
  extra: {
    charset: 'utf8mb4_unicode_ci',
  },
});