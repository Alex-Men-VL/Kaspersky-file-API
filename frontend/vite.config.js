import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from 'path'

const resolvePath = (p) => path.resolve(__dirname, p)

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      app: resolvePath('src/app'),
      configs: resolvePath('src/configs'),
      components: resolvePath('src/components'),
      modules: resolvePath('src/modules'),
      shared: resolvePath('src/shared'),
    }
  }
})
