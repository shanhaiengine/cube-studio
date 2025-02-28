import { TThemeType } from "./theme"

const appLogo = require('./images/logoCB.svg')
const loadingLogo = require('./images/loadingLogo.png')
const supLogo = require('./images/yuekeLogo.svg')

interface IGlobalConfig {
    appLogo: any,
    loadingLogo: any,
    supLogo: any,
    theme: TThemeType,
}

const globalConfig: IGlobalConfig = {
    appLogo,
    loadingLogo,
    supLogo,
    theme: 'star',
}

export default globalConfig