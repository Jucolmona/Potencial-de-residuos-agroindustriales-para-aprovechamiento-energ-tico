# Determinación de la capacidad calorifica

La biomasa es uno de los recursos renovables más abundantes y por esto, el interes mundial de promover la producción de bioenergía cómo alternativa al uso de de combustibles fósiles (FAO, 2011).

## Ruta de conversion de la Biomasa con alto contenido de lignina

Se trata de una ruta de conversión termoquimica 

### Modelos matemáticos

- #### Potencial Geográfico o Geoespacial

Los cultivos de interés energético para la producción de biomasa residual se categorizan en cultivos transitorios y cultivos permanentes. Dentro del primer grupo se encuentran: el arroz y el maiz y dentro del segundo grupo estan el banano, el cafe, la caña de azucar y la panelera, la palma de aceite y el platano.

El potencial energético teórico de la biomasa equivale a la cantidad máxima de energía que está físicamente disponible de una determinada fuente. Para su estimación no se consideran las eficiencias de conversión y pérdidas. Por ello para la estimación del potencial energético se considera la metodología propuesta por (Serrato & Lesmes 2016) en la cual se pueden incluirse las áreas cultivadas. Además el potencial energético de la biomasa se obtiene a a partir de la relación que existe entre la masa de residuo seco $(Mrs)$ y la energía del residuo por unidad de masa $(E)$ también conocido como poder calorífico inferior $(PCI)$. Adicional, este tipo de pontencial puede ser entendido como potencial geográfico o geoespacial. En la siguiente ecuación se expresa la relación entre las variables y se plantea un modelo matemático aproximado:

$$PE = Mrs \cdot E$$

Donde:

- $PE$: potencial energético $[TJ/año$]$
- $E/PCI$: energía del residuo por unidad de masa $[TJ/t]$
- $Mrs$: masa de residuo seco $[t/año]$

La masa del residuo seco se estima a partir de la siguiente ecuación:

$$Mrs = A \cdot Rc \cdot Fr \cdot Yrs$$

Donde

- $A$: Area cultivada $[ha/año]$
- $Rc$: rendimiento del cultivo $[T$ $Producto$ $principal/ha$ $cultivada]$
- $Fr$: factor de residuo de cultivo $[t$ $de$ $residuo/t$ $de$ $producto$ $principal]$
- $Yrs$: fracción de residuo seco $[t$ $residuo$ $seco/t$ $de$ $residuo$ $humedo]$

    - ##### Masa de residuo seco a partir de varios cultivos y varios residuos

$$M_{rs} = A \cdot R_c \cdot \sum_{l=1}^{n} \sum_{k=1}^{m} F_{rs_{k,l}} \cdot Y_{rs_{k,l}}$$

Donde

- $M_{rs}$: Masa de residuo seco
- $A$: Área cultivada [ha/total]
- $R_c$: Rendimiento del cultivo [t del producto principal/ha cultivada]
- $F_{rs_{k,l}}$: Factor de residuo del cultivo $l$ [t de residuo/t de producto principal]
- $Y_{rs_{k,l}}:$ Fracción de residuo seco [t residuo seco/t de residuo húmedo]
- $n$: cantidad de cultivos
- $m$: cantidad de residuos
- $i$: tipo de cultivo (agrícola o 

    - ##### Potencial energético de residuo seco

$$PE_{GEO_{BRA}} = A \cdot R_c \cdot \sum_{l=1}^{n} \sum_{k=1}^{m} F_{rs_{k,l}} \cdot Y_{rs_{k,l}} \cdot PCI_{k,i}$$

Donde:

- $PE_GEO$: Potencial energético [TJ/año] de la biomasa residual agrícola (BRA)
- $A$: Área cultivada [ha/total]
- $R_c$: Rendimiento del cultivo [t del producto principal/ha cultivada]
- $F_{rs_{k,l}}$: Factor de residuo del cultivo $l$ [t de residuo/t de producto principal]
- $Y_{rs_{k,l}}$: Fracción de residuo seco [t residuo seco/t de residuo húmedo]
- $PCI_{k,i}$: PCI inferior del residuo seco [TJ/t]
- $n$: cantidad de cultivos
- $m$: cantidad de residuos
- $i$: tipo de cultivo (agrícola o agroindustrial)
- $k$: tipo de residuos de cosecha

