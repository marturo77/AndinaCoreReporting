# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: cotizacion\carga_manual.feature.spec.js >> R03 Creacion manual de cotizacion >> R03-C02 creacion manual de cotizacion desde archivo
- Location: .features-gen\cotizacion\carga_manual.feature.spec.js:12:7

# Error details

```
Error: No se pudo confirmar que la pagina de cotizacion estuviera lista dentro de 40000 ms. URL actual: https://andinavidasegurospre.linktic.com/cotizaciones/nueva. Texto visible: [sin texto visible]
```

# Test source

```ts
  155 |     } catch {
  156 |       return;
  157 |     }
  158 | 
  159 |     const tiempoLimite = Date.now() + DEFAULT_TIMEOUT;
  160 |     while (Date.now() < tiempoLimite) {
  161 |       if (this.page.isClosed()) {
  162 |         throw new Error('La pagina de cotizacion se cerro mientras se esperaba estabilidad de carga.');
  163 |       }
  164 | 
  165 |       const indicatorVisible = await loadingIndicators
  166 |         .evaluateAll((elements) =>
  167 |           elements.some((element) => {
  168 |             const target = element as HTMLElement;
  169 |             const styles = window.getComputedStyle(target);
  170 |             return (
  171 |               styles.display !== 'none' &&
  172 |               styles.visibility !== 'hidden' &&
  173 |               styles.opacity !== '0' &&
  174 |               target.getAttribute('aria-hidden') !== 'true' &&
  175 |               !!(target.offsetWidth || target.offsetHeight || target.getClientRects().length)
  176 |             );
  177 |           })
  178 |         )
  179 |         .catch(() => false);
  180 |       const contenidoVisible = await contenidoListo.isVisible().catch(() => false);
  181 |       if (contenidoVisible && !indicatorVisible) {
  182 |         await this.page.waitForTimeout(500).catch(() => {});
  183 |         const indicatorStillVisible = await loadingIndicators
  184 |           .evaluateAll((elements) =>
  185 |             elements.some((element) => {
  186 |               const target = element as HTMLElement;
  187 |               const styles = window.getComputedStyle(target);
  188 |               return (
  189 |                 styles.display !== 'none' &&
  190 |                 styles.visibility !== 'hidden' &&
  191 |                 styles.opacity !== '0' &&
  192 |                 target.getAttribute('aria-hidden') !== 'true' &&
  193 |                 !!(target.offsetWidth || target.offsetHeight || target.getClientRects().length)
  194 |               );
  195 |             })
  196 |           )
  197 |           .catch(() => false);
  198 |         if (!indicatorStillVisible) {
  199 |           return;
  200 |         }
  201 |       }
  202 | 
  203 |       await this.page.waitForTimeout(250).catch(() => {});
  204 |     }
  205 | 
  206 |     throw new Error(
  207 |       `La pagina de cotizacion no quedo estable dentro de ${DEFAULT_TIMEOUT} ms. URL actual: ${this.page.url()}`
  208 |     );
  209 |   }
  210 | 
  211 |   private async esperarVistaCotizacionLista(timeoutMs = COTIZACION_OPEN_TIMEOUT): Promise<void> {
  212 |     const limite = Date.now() + timeoutMs;
  213 |     const headingCotizacion = this.page
  214 |       .getByRole('heading', { name: /(Crear|Nueva|Cotizaci.n).*cotizaci.n|Crear cotizaci.n/i })
  215 |       .first();
  216 |     const botonGenerarCotizacion = this.page
  217 |       .getByRole('button', { name: /Generar cotizaci.n/i })
  218 |       .first();
  219 |     let ultimoDiagnostico = '';
  220 | 
  221 |     while (Date.now() < limite) {
  222 |       if (this.page.isClosed()) {
  223 |         throw new Error('La pagina se cerro mientras se esperaba la vista de cotizacion.');
  224 |       }
  225 | 
  226 |       const urlActual = this.page.url();
  227 |       const textoVisible = await this.page.locator('body').innerText().catch(() => '');
  228 |       const textoNormalizado = this.normalizarLabelComparacion(textoVisible);
  229 | 
  230 |       if (this.esPantallaLogin(textoNormalizado)) {
  231 |         throw new Error(
  232 |           `La sesion no quedo autenticada al abrir cotizacion. URL actual: ${urlActual}.`
  233 |         );
  234 |       }
  235 | 
  236 |       if (
  237 |         await botonGenerarCotizacion.isVisible().catch(() => false) ||
  238 |         await headingCotizacion.isVisible().catch(() => false)
  239 |       ) {
  240 |         return;
  241 |       }
  242 | 
  243 |       if (this.esPantallaErrorCotizacion(textoNormalizado)) {
  244 |         throw new Error(
  245 |           `La pagina de cotizacion mostro un error al cargar. URL actual: ${urlActual}. ` +
  246 |           `Texto visible: ${this.resumirTextoDiagnostico(textoVisible)}`
  247 |         );
  248 |       }
  249 | 
  250 |       ultimoDiagnostico =
  251 |         `URL actual: ${urlActual}. Texto visible: ${this.resumirTextoDiagnostico(textoVisible)}`;
  252 |       await this.page.waitForTimeout(500).catch(() => {});
  253 |     }
  254 | 
> 255 |     throw new Error(
      |           ^ Error: No se pudo confirmar que la pagina de cotizacion estuviera lista dentro de 40000 ms. URL actual: https://andinavidasegurospre.linktic.com/cotizaciones/nueva. Texto visible: [sin texto visible]
  256 |       `No se pudo confirmar que la pagina de cotizacion estuviera lista dentro de ${timeoutMs} ms. ` +
  257 |       ultimoDiagnostico
  258 |     );
  259 |   }
  260 | 
  261 |   async fillTextField(
  262 |     section: FormSection,
  263 |     nombreCampo: string,
  264 |     valor: string | number | undefined
  265 |   ): Promise<void> {
  266 |     if (valor == null) {
  267 |       return;
  268 |     }
  269 | 
  270 |     const valorTexto = String(valor);
  271 |     const normalizedName = this.normalizarTexto(nombreCampo);
  272 |     const textMatch = `contains(${this.translateXpath('normalize-space(text())')}, '${normalizedName}')`;
  273 | 
  274 |     try {
  275 |       const field = await this.resolverCampoTexto(this.page, nombreCampo, textMatch, normalizedName, section);
  276 |       const readonly = await field.evaluate((element) =>
  277 |         element.hasAttribute('readonly')
  278 |       );
  279 |       const disabled = await field.evaluate((element) =>
  280 |         element.hasAttribute('disabled')
  281 |       );
  282 | 
  283 |       if (readonly || disabled) {
  284 |         await field.evaluate((element, inputValue) => {
  285 |           const target = element as HTMLInputElement | HTMLTextAreaElement;
  286 |           target.value = String(inputValue);
  287 |           target.dispatchEvent(new Event('input', { bubbles: true }));
  288 |           target.dispatchEvent(new Event('change', { bubbles: true }));
  289 |           target.dispatchEvent(new Event('blur', { bubbles: true }));
  290 |         }, valorTexto);
  291 | 
  292 |         if (await this.campoContieneValorEsperado(field, valorTexto)) {
  293 |           return;
  294 |         }
  295 | 
  296 |         if (!disabled && this.debeUsarCalendario(nombreCampo, valorTexto)) {
  297 |           await field.click({ timeout: 10000, force: true });
  298 |           await this.navegarYSeleccionarFecha(valorTexto);
  299 |           return;
  300 |         }
  301 | 
  302 |         return;
  303 |       }
  304 | 
  305 |       await this.escribirValorEnCampo(field, valorTexto, nombreCampo);
  306 |     } catch (error) {
  307 |       throw new Error(
  308 |         `Fallo al diligenciar el campo '${nombreCampo}' con el valor '${valorTexto}': ${error}`
  309 |       );
  310 |     }
  311 |   }
  312 | 
  313 |   async fillDateField(
  314 |     section: FormSection,
  315 |     nombreCampo: string,
  316 |     valor: string
  317 |   ): Promise<void> {
  318 |     if (!valor?.trim()) {
  319 |       throw new Error(`No se recibio un valor valido para el campo '${nombreCampo}'.`);
  320 |     }
  321 | 
  322 |     const valorTexto = valor.trim().replace(/-/g, '/');
  323 |     const normalizedName = this.normalizarTexto(nombreCampo);
  324 |     const textMatch = `contains(${this.translateXpath('normalize-space(text())')}, '${normalizedName}')`;
  325 |     try {
  326 |       const field = await this.resolverCampoTexto(this.page, nombreCampo, textMatch, normalizedName, section);
  327 |       const targetField = (await field.evaluate((element) => element.tagName.toLowerCase()) === 'input')
  328 |         ? field
  329 |         : field.locator('input').first();
  330 |       await targetField.scrollIntoViewIfNeeded();
  331 |       await this.escribirFechaEnCampo(targetField, valorTexto, nombreCampo);
  332 |     } catch (error) {
  333 |       throw new Error(
  334 |         `Fallo al diligenciar la fecha '${nombreCampo}' con el valor '${valorTexto}': ${error}`
  335 |       );
  336 |     }
  337 |   }
  338 | 
  339 |   async guardarCotizacion(_context: any): Promise<void> {
  340 |     console.log('Guardando cotizacion manual...');
  341 |     await this.page.waitForTimeout(1000);
  342 |     await this.clickBoton('Guardar');
  343 |   }
  344 | 
  345 |   async isLoaded(timeout: number = 20): Promise<boolean> {
  346 |     try {
  347 |       const timeoutMs = timeout * 1000;
  348 |       await this.page.waitForLoadState('domcontentloaded', { timeout: timeoutMs });
  349 |       await this.page.locator('body').waitFor({ state: 'visible', timeout: timeoutMs });
  350 |       await this.page
  351 |         .locator('.q-spinner, .q-spinner-mat')
  352 |         .first()
  353 |         .waitFor({ state: 'hidden', timeout: 2_000 })
  354 |         .catch(() => {});
  355 |       return true;
```