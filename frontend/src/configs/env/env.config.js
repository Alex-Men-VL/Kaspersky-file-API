import {commonConfig} from './common.config'

class EnvConfig {
  static instance = null
  config = {}

  validate(config) {
    for (const [key, value] of Object.entries(config)) {
      if (typeof value === 'undefined') {
        throw new Error(`Missing key "${key}" in import.meta.env`)
      }
    }
    return config
  }

  constructor() {
    this.config = this.validate(commonConfig)
  }

  static getInstance(configs) {
    if (!EnvConfig.instance) {
      EnvConfig.instance = new EnvConfig(configs)
    }
    return EnvConfig.instance
  }

  get(key) {
    return this.config[key]
  }
}

export const env = EnvConfig.getInstance()
