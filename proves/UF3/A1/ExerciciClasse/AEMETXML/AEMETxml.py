'''
Descarregar XML de la predicció detallada de Tossa de Mar (de la setmana actual )

Fer un programa en Python que a partir del fitxer XML, calculi, i mostri per pantalla:

Probabilitat de precipitació

Temperatura mitjana

<?xml version='1.0' encoding='ISO-8859-15'?>
<root xmlns:xsd="https://www.w3.org/2001/XMLSchema" xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" id="17202" version="1.0" xsi:noNamespaceSchemaLocation="https://www.aemet.es/xsd/localidades.xsd">
  <origen>
    <productor>Agencia Estatal de Meteorología - AEMET. Gobierno de España</productor>
    <web>https://www.aemet.es</web>
    <enlace>https://www.aemet.es/es/eltiempo/prediccion/municipios/tossa-de-mar-id17202</enlace>
    <language>es</language>
    <copyright>© AEMET. Autorizado el uso de la información y su reproducción citando a AEMET como autora de la misma.</copyright>
    <nota_legal>https://www.aemet.es/es/nota_legal</nota_legal>
  </origen>
  <elaborado>2024-04-25T10:00:15</elaborado>
  <nombre>Tossa de Mar</nombre>
  <provincia>Girona</provincia>
  <prediccion>
    <dia fecha="2024-04-25">
      <prob_precipitacion periodo="00-24"/>
      <prob_precipitacion periodo="00-12"/>
      <prob_precipitacion periodo="12-24">65</prob_precipitacion>
      <prob_precipitacion periodo="00-06"/>
      <prob_precipitacion periodo="06-12">60</prob_precipitacion>
      <prob_precipitacion periodo="12-18">25</prob_precipitacion>
      <prob_precipitacion periodo="18-24">25</prob_precipitacion>
      <cota_nieve_prov periodo="00-24"></cota_nieve_prov>
      <cota_nieve_prov periodo="00-12"></cota_nieve_prov>
      <cota_nieve_prov periodo="12-24">1600</cota_nieve_prov>
      <cota_nieve_prov periodo="00-06"></cota_nieve_prov>
      <cota_nieve_prov periodo="06-12">1500</cota_nieve_prov>
      <cota_nieve_prov periodo="12-18">1600</cota_nieve_prov>
      <cota_nieve_prov periodo="18-24">1700</cota_nieve_prov>
      <estado_cielo periodo="00-24" descripcion=""/>
      <estado_cielo periodo="00-12" descripcion=""/>
      <estado_cielo periodo="12-24" descripcion="Muy nuboso con lluvia escasa">45</estado_cielo>
      <estado_cielo periodo="00-06" descripcion=""/>
      <estado_cielo periodo="06-12" descripcion="Muy nuboso con lluvia escasa">45</estado_cielo>
      <estado_cielo periodo="12-18" descripcion="Muy nuboso con lluvia escasa">45</estado_cielo>
      <estado_cielo periodo="18-24" descripcion="Muy nuboso">15</estado_cielo>
      <viento periodo="00-24">
        <direccion></direccion>
        <velocidad></velocidad>
      </viento>
      <viento periodo="00-12">
        <direccion></direccion>
        <velocidad></velocidad>
      </viento>
      <viento periodo="12-24">
        <direccion>S</direccion>
        <velocidad>10</velocidad>
      </viento>
      <viento periodo="00-06">
        <direccion>NO</direccion>
        <velocidad>5</velocidad>
      </viento>
      <viento periodo="06-12">
        <direccion>SE</direccion>
        <velocidad>10</velocidad>
      </viento>
      <viento periodo="12-18">
        <direccion>S</direccion>
        <velocidad>10</velocidad>
      </viento>
      <viento periodo="18-24">
        <direccion>C</direccion>
        <velocidad>0</velocidad>
      </viento>
      <racha_max periodo="00-24"/>
      <racha_max periodo="00-12"/>
      <racha_max periodo="12-24"/>
      <racha_max periodo="00-06"/>
      <racha_max periodo="06-12"/>
      <racha_max periodo="12-18"/>
      <racha_max periodo="18-24"/>
      <temperatura>
        <maxima>16</maxima>
        <minima>9</minima>
        <dato hora="06">10</dato>
        <dato hora="12">15</dato>
        <dato hora="18">14</dato>
        <dato hora="24">10</dato>
      </temperatura>
      <sens_termica>
        <maxima>16</maxima>
        <minima>9</minima>
        <dato hora="06">10</dato>
        <dato hora="12">15</dato>
        <dato hora="18">14</dato>
        <dato hora="24">10</dato>
      </sens_termica>
      <humedad_relativa>
        <maxima>95</maxima>
        <minima>50</minima>
        <dato hora="06">70</dato>
        <dato hora="12">50</dato>
        <dato hora="18">70</dato>
        <dato hora="24">95</dato>
      </humedad_relativa>
      <uv_max>5</uv_max>
    </dia>
    <dia fecha="2024-04-26">
      <prob_precipitacion periodo="00-24">100</prob_precipitacion>
      <prob_precipitacion periodo="00-12">70</prob_precipitacion>
      <prob_precipitacion periodo="12-24">90</prob_precipitacion>
      <prob_precipitacion periodo="00-06">0</prob_precipitacion>
      <prob_precipitacion periodo="06-12">70</prob_precipitacion>
      <prob_precipitacion periodo="12-18">70</prob_precipitacion>
      <prob_precipitacion periodo="18-24">50</prob_precipitacion>
      <cota_nieve_prov periodo="00-24">1800</cota_nieve_prov>
      <cota_nieve_prov periodo="00-12">1700</cota_nieve_prov>
      <cota_nieve_prov periodo="12-24">1900</cota_nieve_prov>
      <cota_nieve_prov periodo="00-06"></cota_nieve_prov>
      <cota_nieve_prov periodo="06-12">1700</cota_nieve_prov>
      <cota_nieve_prov periodo="12-18">1800</cota_nieve_prov>
      <cota_nieve_prov periodo="18-24">1900</cota_nieve_prov>
      <estado_cielo periodo="00-24" descripcion="Intervalos nubosos con lluvia escasa">43</estado_cielo>
      <estado_cielo periodo="00-12" descripcion="Intervalos nubosos con lluvia escasa">43</estado_cielo>
      <estado_cielo periodo="12-24" descripcion="Intervalos nubosos con lluvia escasa">43</estado_cielo>
      <estado_cielo periodo="00-06" descripcion="Poco nuboso">12n</estado_cielo>
      <estado_cielo periodo="06-12" descripcion="Intervalos nubosos con lluvia escasa">43</estado_cielo>
      <estado_cielo periodo="12-18" descripcion="Intervalos nubosos con lluvia escasa">43</estado_cielo>
      <estado_cielo periodo="18-24" descripcion="Muy nuboso">15</estado_cielo>
      <viento periodo="00-24">
        <direccion>S</direccion>
        <velocidad>15</velocidad>
      </viento>
      <viento periodo="00-12">
        <direccion>S</direccion>
        <velocidad>15</velocidad>
      </viento>
      <viento periodo="12-24">
        <direccion>S</direccion>
        <velocidad>15</velocidad>
      </viento>
      <viento periodo="00-06">
        <direccion>C</direccion>
        <velocidad>0</velocidad>
      </viento>
      <viento periodo="06-12">
        <direccion>S</direccion>
        <velocidad>15</velocidad>
      </viento>
      <viento periodo="12-18">
        <direccion>S</direccion>
        <velocidad>10</velocidad>
      </viento>
      <viento periodo="18-24">
        <direccion>SE</direccion>
        <velocidad>15</velocidad>
      </viento>
      <racha_max periodo="00-24"/>
      <racha_max periodo="00-12"/>
      <racha_max periodo="12-24"/>
      <racha_max periodo="00-06"/>
      <racha_max periodo="06-12"/>
      <racha_max periodo="12-18"/>
      <racha_max periodo="18-24"/>
      <temperatura>
        <maxima>18</maxima>
        <minima>8</minima>
        <dato hora="06">9</dato>
        <dato hora="12">16</dato>
        <dato hora="18">15</dato>
        <dato hora="24">13</dato>
      </temperatura>
      <sens_termica>
        <maxima>18</maxima>
        <minima>7</minima>
        <dato hora="06">9</dato>
        <dato hora="12">16</dato>
        <dato hora="18">15</dato>
        <dato hora="24">13</dato>
      </sens_termica>
      <humedad_relativa>
        <maxima>100</maxima>
        <minima>65</minima>
        <dato hora="06">95</dato>
        <dato hora="12">65</dato>
        <dato hora="18">80</dato>
        <dato hora="24">100</dato>
      </humedad_relativa>
      <uv_max>5</uv_max>
    </dia>
    <dia fecha="2024-04-27">
      <prob_precipitacion periodo="00-24">100</prob_precipitacion>
      <prob_precipitacion periodo="00-12">100</prob_precipitacion>
      <prob_precipitacion periodo="12-24">95</prob_precipitacion>
      <cota_nieve_prov periodo="00-24">2000</cota_nieve_prov>
      <cota_nieve_prov periodo="00-12">1900</cota_nieve_prov>
      <cota_nieve_prov periodo="12-24">2000</cota_nieve_prov>
      <estado_cielo periodo="00-24" descripcion="Nuboso con lluvia">24</estado_cielo>
      <estado_cielo periodo="00-12" descripcion="Muy nuboso con lluvia">25</estado_cielo>
      <estado_cielo periodo="12-24" descripcion="Intervalos nubosos con lluvia">23</estado_cielo>
      <viento periodo="00-24">
        <direccion>S</direccion>
        <velocidad>25</velocidad>
      </viento>
      <viento periodo="00-12">
        <direccion>S</direccion>
        <velocidad>25</velocidad>
      </viento>
      <viento periodo="12-24">
        <direccion>S</direccion>
        <velocidad>25</velocidad>
      </viento>
      <racha_max periodo="00-24">55</racha_max>
      <racha_max periodo="00-12">55</racha_max>
      <racha_max periodo="12-24">55</racha_max>
      <temperatura>
        <maxima>19</maxima>
        <minima>13</minima>
      </temperatura>
      <sens_termica>
        <maxima>19</maxima>
        <minima>13</minima>
      </sens_termica>
      <humedad_relativa>
        <maxima>100</maxima>
        <minima>70</minima>
      </humedad_relativa>
      <uv_max>6</uv_max>
    </dia>
    <dia fecha="2024-04-28">
      <prob_precipitacion periodo="00-24">100</prob_precipitacion>
      <prob_precipitacion periodo="00-12">100</prob_precipitacion>
      <prob_precipitacion periodo="12-24">100</prob_precipitacion>
      <cota_nieve_prov periodo="00-24">2200</cota_nieve_prov>
      <cota_nieve_prov periodo="00-12">2100</cota_nieve_prov>
      <cota_nieve_prov periodo="12-24">2200</cota_nieve_prov>
      <estado_cielo periodo="00-24" descripcion="Muy nuboso con lluvia">25</estado_cielo>
      <estado_cielo periodo="00-12" descripcion="Cubierto con lluvia">26</estado_cielo>
      <estado_cielo periodo="12-24" descripcion="Muy nuboso con lluvia">25</estado_cielo>
      <viento periodo="00-24">
        <direccion>SE</direccion>
        <velocidad>15</velocidad>
      </viento>
      <viento periodo="00-12">
        <direccion>S</direccion>
        <velocidad>15</velocidad>
      </viento>
      <viento periodo="12-24">
        <direccion>SE</direccion>
        <velocidad>15</velocidad>
      </viento>
      <racha_max periodo="00-24"/>
      <racha_max periodo="00-12"/>
      <racha_max periodo="12-24"/>
      <temperatura>
        <maxima>18</maxima>
        <minima>12</minima>
      </temperatura>
      <sens_termica>
        <maxima>18</maxima>
        <minima>12</minima>
      </sens_termica>
      <humedad_relativa>
        <maxima>100</maxima>
        <minima>80</minima>
      </humedad_relativa>
      <uv_max>6</uv_max>
    </dia>
    <dia fecha="2024-04-29">
      <prob_precipitacion>100</prob_precipitacion>
      <cota_nieve_prov>2400</cota_nieve_prov>
      <estado_cielo descripcion="Cubierto con lluvia">26</estado_cielo>
      <viento>
        <direccion>NE</direccion>
        <velocidad>20</velocidad>
      </viento>
      <racha_max>45</racha_max>
      <temperatura>
        <maxima>17</maxima>
        <minima>12</minima>
      </temperatura>
      <sens_termica>
        <maxima>17</maxima>
        <minima>12</minima>
      </sens_termica>
      <humedad_relativa>
        <maxima>100</maxima>
        <minima>80</minima>
      </humedad_relativa>
      <uv_max>6</uv_max>
    </dia>
    <dia fecha="2024-04-30">
      <prob_precipitacion>95</prob_precipitacion>
      <cota_nieve_prov>2300</cota_nieve_prov>
      <estado_cielo descripcion="Cubierto con lluvia">26</estado_cielo>
      <viento>
        <direccion>NE</direccion>
        <velocidad>15</velocidad>
      </viento>
      <racha_max/>
      <temperatura>
        <maxima>18</maxima>
        <minima>12</minima>
      </temperatura>
      <sens_termica>
        <maxima>18</maxima>
        <minima>12</minima>
      </sens_termica>
      <humedad_relativa>
        <maxima>100</maxima>
        <minima>75</minima>
      </humedad_relativa>
    </dia>
    <dia fecha="2024-05-01">
      <prob_precipitacion>65</prob_precipitacion>
      <cota_nieve_prov>2000</cota_nieve_prov>
      <estado_cielo descripcion="Muy nuboso con lluvia">25</estado_cielo>
      <viento>
        <direccion>S</direccion>
        <velocidad>15</velocidad>
      </viento>
      <racha_max/>
      <temperatura>
        <maxima>19</maxima>
        <minima>10</minima>
      </temperatura>
      <sens_termica>
        <maxima>19</maxima>
        <minima>10</minima>
      </sens_termica>
      <humedad_relativa>
        <maxima>90</maxima>
        <minima>60</minima>
      </humedad_relativa>
    </dia>
  </prediccion>
</root>

'''
import xml.etree.ElementTree as ET
def aemetxml(nomarxiu):
    tree = ET.parse(nomarxiu)
    root = tree.getroot()
    dia = root.find('prediccion/dia')
    prob_precipitacion = dia.find('prob_precipitacion').text
    temperatura = dia.find('temperatura')
    maxima = temperatura.find('maxima').text
    minima = temperatura.find('minima').text
    return prob_precipitacion, maxima, minima

nomarxiu = 'localidad_17202.xml'
prob_precipitacion, maxima, minima = aemetxml(nomarxiu)
print(f'Probabilitat de precipitació: {prob_precipitacion}')
print(f'Temperatura mitjana: {maxima} - {minima} = {(int(maxima) + int(minima)) / 2}')

