(ns hermes-api.components
  (:require [com.stuartsierra.component :as component]
            [hermes-api.components.service :as service]))

(def base []
  (component/system-map
   :service (component/using (service/new-service) [])))