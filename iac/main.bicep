var appServicePlanName = 'trip-hosting-plan'
var sku = 'S1'
var location = resourceGroup().location


resource appServicePlan 'Microsoft.Web/serverfarms@2020-06-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: sku
  }
  kind: 'app,linux'
  properties: {
    reserved: true
  }
}

resource tripapp 'Microsoft.Web/sites@2021-01-15' = {
  name: 'trip-app-sruinard'
  location: resourceGroup().location
  properties: {
    serverFarmId: appServicePlan.id
    httpsOnly: true
    appCommandLine: 'startup.sh'
    siteConfig: {
      minTlsVersion: '1.2'
      linuxFxVersion: 'python|3.8'
      appSettings: [
        {
          name: 'APPINSIGHTS_INSTRUMENTATIONKEY'
          value: appInsights.properties.InstrumentationKey
        }
      ]
    }
  }
}

resource tripAppSettings 'Microsoft.Web/sites/config@2021-01-15' = {
  name: '${tripapp.name}/appsettings'
  properties: {
    APPINSIGHTS_INSTRUMENTATIONKEY: appInsights.properties.InstrumentationKey
    DBCONNECTION_STRING: 'teststring'
  }
}

resource tripAppLogging 'Microsoft.Web/sites/config@2021-01-15' = {
  name: '${tripapp.name}/logs'
  properties: {
    appCommandLine: 'startup.sh'
    applicationLogs: {
      fileSystem: {
        level: 'Warning'
      }
    }
    httpLogs: {
      fileSystem: {
        retentionInMb: 40
        enabled: true
      }
    }
    failedRequestsTracing: {
      enabled: true
    }
    detailedErrorMessages: {
      enabled: true
    }
  }
}

// log workspace
resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2021-06-01' = {
  name: 'trip-workspace'
  location: resourceGroup().location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

// Insights
resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'trip-appinsights'
  location: resourceGroup().location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalyticsWorkspace.id
  }
}
