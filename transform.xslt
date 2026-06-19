<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>


  <xsl:template match="/">
    <html>
      <head>
        <meta charset="UTF-8"/>
        <title>Rapport d'Analyse ML - Supermarché</title>
        <style>
          body {
            font-family: Arial, sans-serif;
            margin: 30px;
            background-color: #f5f5f5;
          }
          h1 {
            color: #2c3e50;
            text-align: center;
          }
          h2 {
            color: #34495e;
            margin-top: 30px;
          }

          /*
          .kpi-table {
            width: 60%;
            margin: 20px auto;
            border-collapse: collapse;
            background-color: #ffffff;
          }
          .kpi-table th {
            background-color: #2c3e50;
            color: white;
            padding: 10px;
            text-align: left;
          }
          .kpi-table td {
            padding: 8px 10px;
            border: 1px solid #ccc;
          }

          /* ── Tableau des transactions ── */
          .data-table {
            width: 100%;
            border-collapse: collapse;
            background-color: #ffffff;
            margin-top: 10px;
          }
          .data-table th {
            background-color: #2c3e50;
            color: white;
            padding: 8px;
            text-align: left;
          }
          .data-table td {
            padding: 6px 8px;
            border: 1px solid #ddd;
          }
          .data-table tr:nth-child(even) {
            background-color: #f2f2f2;
          }

          
          .anomalie    { color: red;    font-weight: bold; }
          .normal      { color: green;  }
          .total-high  { color: green;  font-weight: bold; }
          .total-mid   { color: orange; }
          .total-low   { color: gray;   }
          .seg-petit   { color: gray;   }
          .seg-moyen   { color: blue;   }
          .seg-gros    { color: #e67e22; font-weight: bold; }
        </style>
      </head>
      <body>

        <h1>Rapport d'Analyse ML - Supermarché</h1>

        
        <h2>KPI Globaux</h2>
        <table class="kpi-table">
          <tr>
            <th>Indicateur</th>
            <th>Valeur</th>
          </tr>
          <tr>
            <td>Nombre total de transactions</td>
            <td><xsl:value-of select="count(//Resultat)"/></td>
          </tr>
          <tr>
            <td>Nombre d'anomalies détectées</td>
            <td><xsl:value-of select="count(//Resultat[anomalie='Anomalie'])"/></td>
          </tr>
          <tr>
            <td>Nombre de transactions normales</td>
            <td><xsl:value-of select="count(//Resultat[anomalie='Normal'])"/></td>
          </tr>
          <tr>
            <td>Segment : Petit acheteur</td>
            <td><xsl:value-of select="count(//Resultat[nom_segment='Petit acheteur'])"/></td>
          </tr>
          <tr>
            <td>Segment : Acheteur moyen</td>
            <td><xsl:value-of select="count(//Resultat[nom_segment='Acheteur moyen'])"/></td>
          </tr>
          <tr>
            <td>Segment : Gros acheteur</td>
            <td><xsl:value-of select="count(//Resultat[nom_segment='Gros acheteur'])"/></td>
          </tr>
        </table>

        
        <h2>Détail des transactions</h2>
        <table class="data-table">
          <thead>
            <tr>
              <th>Invoice ID</th>
              <th>Branche</th>
              <th>Ville</th>
              <th>Type client</th>
              <th>Genre</th>
              <th>Produit</th>
              <th>Prix unitaire</th>
              <th>Quantité</th>
              <th>Total</th>
              <th>Date</th>
              <th>Paiement</th>
              <th>Rating</th>
              <th>Anomalie</th>
              <th>Segment</th>
            </tr>
          </thead>
          <tbody>

            <!-- xsl:for-each : parcourt chaque élément Resultat -->
            <xsl:for-each select="//Resultat">
              <tr>
                <td><xsl:value-of select="Invoice_ID"/></td>
                <td><xsl:value-of select="Branch"/></td>
                <td><xsl:value-of select="City"/></td>
                <td><xsl:value-of select="Customer_type"/></td>
                <td><xsl:value-of select="Gender"/></td>
                <td><xsl:value-of select="Product_line"/></td>
                <td><xsl:value-of select="Unit_price"/> DH</td>
                <td><xsl:value-of select="Quantity"/></td>

                
                <td>
                  <xsl:choose>
                    <xsl:when test="Total &gt; 400">
                      <span class="total-high"><xsl:value-of select="Total"/> DH</span>
                    </xsl:when>
                    <xsl:when test="Total &gt; 150">
                      <span class="total-mid"><xsl:value-of select="Total"/> DH</span>
                    </xsl:when>
                    <xsl:otherwise>
                      <span class="total-low"><xsl:value-of select="Total"/> DH</span>
                    </xsl:otherwise>
                  </xsl:choose>
                </td>

                <td><xsl:value-of select="Date"/></td>
                <td><xsl:value-of select="Payment"/></td>
                <td><xsl:value-of select="Rating"/></td>

                <!-- Couleur conditionnelle sur l'anomalie -->
                <td>
                  <xsl:choose>
                    <xsl:when test="anomalie='Anomalie'">
                      <span class="anomalie">Anomalie</span>
                    </xsl:when>
                    <xsl:otherwise>
                      <span class="normal">Normal</span>
                    </xsl:otherwise>
                  </xsl:choose>
                </td>

                
                <td>
                  <xsl:choose>
                    <xsl:when test="nom_segment='Gros acheteur'">
                      <span class="seg-gros"><xsl:value-of select="nom_segment"/></span>
                    </xsl:when>
                    <xsl:when test="nom_segment='Acheteur moyen'">
                      <span class="seg-moyen"><xsl:value-of select="nom_segment"/></span>
                    </xsl:when>
                    <xsl:otherwise>
                      <span class="seg-petit"><xsl:value-of select="nom_segment"/></span>
                    </xsl:otherwise>
                  </xsl:choose>
                </td>

              </tr>
            </xsl:for-each>

          </tbody>
        </table>

        
        <p style="text-align:center; color:gray; margin-top:30px;">
          Rapport généré automatiquement par transformation XSLT
        </p>

      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
