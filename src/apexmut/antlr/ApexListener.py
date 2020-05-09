# Generated from grammar/Apex.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ApexParser import ApexParser
else:
    from ApexParser import ApexParser

# This class defines a complete listener for a parse tree produced by ApexParser.
class ApexListener(ParseTreeListener):

    # Enter a parse tree produced by ApexParser#compilationUnit.
    def enterCompilationUnit(self, ctx:ApexParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by ApexParser#compilationUnit.
    def exitCompilationUnit(self, ctx:ApexParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by ApexParser#packageDeclaration.
    def enterPackageDeclaration(self, ctx:ApexParser.PackageDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#packageDeclaration.
    def exitPackageDeclaration(self, ctx:ApexParser.PackageDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#importDeclaration.
    def enterImportDeclaration(self, ctx:ApexParser.ImportDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#importDeclaration.
    def exitImportDeclaration(self, ctx:ApexParser.ImportDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:ApexParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:ApexParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#modifier.
    def enterModifier(self, ctx:ApexParser.ModifierContext):
        pass

    # Exit a parse tree produced by ApexParser#modifier.
    def exitModifier(self, ctx:ApexParser.ModifierContext):
        pass


    # Enter a parse tree produced by ApexParser#classOrInterfaceModifier.
    def enterClassOrInterfaceModifier(self, ctx:ApexParser.ClassOrInterfaceModifierContext):
        pass

    # Exit a parse tree produced by ApexParser#classOrInterfaceModifier.
    def exitClassOrInterfaceModifier(self, ctx:ApexParser.ClassOrInterfaceModifierContext):
        pass


    # Enter a parse tree produced by ApexParser#variableModifier.
    def enterVariableModifier(self, ctx:ApexParser.VariableModifierContext):
        pass

    # Exit a parse tree produced by ApexParser#variableModifier.
    def exitVariableModifier(self, ctx:ApexParser.VariableModifierContext):
        pass


    # Enter a parse tree produced by ApexParser#classDeclaration.
    def enterClassDeclaration(self, ctx:ApexParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#classDeclaration.
    def exitClassDeclaration(self, ctx:ApexParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#typeParameters.
    def enterTypeParameters(self, ctx:ApexParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by ApexParser#typeParameters.
    def exitTypeParameters(self, ctx:ApexParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by ApexParser#typeParameter.
    def enterTypeParameter(self, ctx:ApexParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by ApexParser#typeParameter.
    def exitTypeParameter(self, ctx:ApexParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by ApexParser#typeBound.
    def enterTypeBound(self, ctx:ApexParser.TypeBoundContext):
        pass

    # Exit a parse tree produced by ApexParser#typeBound.
    def exitTypeBound(self, ctx:ApexParser.TypeBoundContext):
        pass


    # Enter a parse tree produced by ApexParser#enumDeclaration.
    def enterEnumDeclaration(self, ctx:ApexParser.EnumDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#enumDeclaration.
    def exitEnumDeclaration(self, ctx:ApexParser.EnumDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#enumConstants.
    def enterEnumConstants(self, ctx:ApexParser.EnumConstantsContext):
        pass

    # Exit a parse tree produced by ApexParser#enumConstants.
    def exitEnumConstants(self, ctx:ApexParser.EnumConstantsContext):
        pass


    # Enter a parse tree produced by ApexParser#enumConstant.
    def enterEnumConstant(self, ctx:ApexParser.EnumConstantContext):
        pass

    # Exit a parse tree produced by ApexParser#enumConstant.
    def exitEnumConstant(self, ctx:ApexParser.EnumConstantContext):
        pass


    # Enter a parse tree produced by ApexParser#enumBodyDeclarations.
    def enterEnumBodyDeclarations(self, ctx:ApexParser.EnumBodyDeclarationsContext):
        pass

    # Exit a parse tree produced by ApexParser#enumBodyDeclarations.
    def exitEnumBodyDeclarations(self, ctx:ApexParser.EnumBodyDeclarationsContext):
        pass


    # Enter a parse tree produced by ApexParser#interfaceDeclaration.
    def enterInterfaceDeclaration(self, ctx:ApexParser.InterfaceDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#interfaceDeclaration.
    def exitInterfaceDeclaration(self, ctx:ApexParser.InterfaceDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#typeList.
    def enterTypeList(self, ctx:ApexParser.TypeListContext):
        pass

    # Exit a parse tree produced by ApexParser#typeList.
    def exitTypeList(self, ctx:ApexParser.TypeListContext):
        pass


    # Enter a parse tree produced by ApexParser#classBody.
    def enterClassBody(self, ctx:ApexParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by ApexParser#classBody.
    def exitClassBody(self, ctx:ApexParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by ApexParser#interfaceBody.
    def enterInterfaceBody(self, ctx:ApexParser.InterfaceBodyContext):
        pass

    # Exit a parse tree produced by ApexParser#interfaceBody.
    def exitInterfaceBody(self, ctx:ApexParser.InterfaceBodyContext):
        pass


    # Enter a parse tree produced by ApexParser#classBodyDeclaration.
    def enterClassBodyDeclaration(self, ctx:ApexParser.ClassBodyDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#classBodyDeclaration.
    def exitClassBodyDeclaration(self, ctx:ApexParser.ClassBodyDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:ApexParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:ApexParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#methodDeclaration.
    def enterMethodDeclaration(self, ctx:ApexParser.MethodDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#methodDeclaration.
    def exitMethodDeclaration(self, ctx:ApexParser.MethodDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#genericMethodDeclaration.
    def enterGenericMethodDeclaration(self, ctx:ApexParser.GenericMethodDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#genericMethodDeclaration.
    def exitGenericMethodDeclaration(self, ctx:ApexParser.GenericMethodDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:ApexParser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:ApexParser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#genericConstructorDeclaration.
    def enterGenericConstructorDeclaration(self, ctx:ApexParser.GenericConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#genericConstructorDeclaration.
    def exitGenericConstructorDeclaration(self, ctx:ApexParser.GenericConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#fieldDeclaration.
    def enterFieldDeclaration(self, ctx:ApexParser.FieldDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#fieldDeclaration.
    def exitFieldDeclaration(self, ctx:ApexParser.FieldDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#propertyDeclaration.
    def enterPropertyDeclaration(self, ctx:ApexParser.PropertyDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#propertyDeclaration.
    def exitPropertyDeclaration(self, ctx:ApexParser.PropertyDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#propertyBodyDeclaration.
    def enterPropertyBodyDeclaration(self, ctx:ApexParser.PropertyBodyDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#propertyBodyDeclaration.
    def exitPropertyBodyDeclaration(self, ctx:ApexParser.PropertyBodyDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#interfaceBodyDeclaration.
    def enterInterfaceBodyDeclaration(self, ctx:ApexParser.InterfaceBodyDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#interfaceBodyDeclaration.
    def exitInterfaceBodyDeclaration(self, ctx:ApexParser.InterfaceBodyDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#interfaceMemberDeclaration.
    def enterInterfaceMemberDeclaration(self, ctx:ApexParser.InterfaceMemberDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#interfaceMemberDeclaration.
    def exitInterfaceMemberDeclaration(self, ctx:ApexParser.InterfaceMemberDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#constDeclaration.
    def enterConstDeclaration(self, ctx:ApexParser.ConstDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#constDeclaration.
    def exitConstDeclaration(self, ctx:ApexParser.ConstDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#constantDeclarator.
    def enterConstantDeclarator(self, ctx:ApexParser.ConstantDeclaratorContext):
        pass

    # Exit a parse tree produced by ApexParser#constantDeclarator.
    def exitConstantDeclarator(self, ctx:ApexParser.ConstantDeclaratorContext):
        pass


    # Enter a parse tree produced by ApexParser#interfaceMethodDeclaration.
    def enterInterfaceMethodDeclaration(self, ctx:ApexParser.InterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#interfaceMethodDeclaration.
    def exitInterfaceMethodDeclaration(self, ctx:ApexParser.InterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#genericInterfaceMethodDeclaration.
    def enterGenericInterfaceMethodDeclaration(self, ctx:ApexParser.GenericInterfaceMethodDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#genericInterfaceMethodDeclaration.
    def exitGenericInterfaceMethodDeclaration(self, ctx:ApexParser.GenericInterfaceMethodDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#variableDeclarators.
    def enterVariableDeclarators(self, ctx:ApexParser.VariableDeclaratorsContext):
        pass

    # Exit a parse tree produced by ApexParser#variableDeclarators.
    def exitVariableDeclarators(self, ctx:ApexParser.VariableDeclaratorsContext):
        pass


    # Enter a parse tree produced by ApexParser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:ApexParser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by ApexParser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:ApexParser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by ApexParser#variableDeclaratorId.
    def enterVariableDeclaratorId(self, ctx:ApexParser.VariableDeclaratorIdContext):
        pass

    # Exit a parse tree produced by ApexParser#variableDeclaratorId.
    def exitVariableDeclaratorId(self, ctx:ApexParser.VariableDeclaratorIdContext):
        pass


    # Enter a parse tree produced by ApexParser#variableInitializer.
    def enterVariableInitializer(self, ctx:ApexParser.VariableInitializerContext):
        pass

    # Exit a parse tree produced by ApexParser#variableInitializer.
    def exitVariableInitializer(self, ctx:ApexParser.VariableInitializerContext):
        pass


    # Enter a parse tree produced by ApexParser#arrayInitializer.
    def enterArrayInitializer(self, ctx:ApexParser.ArrayInitializerContext):
        pass

    # Exit a parse tree produced by ApexParser#arrayInitializer.
    def exitArrayInitializer(self, ctx:ApexParser.ArrayInitializerContext):
        pass


    # Enter a parse tree produced by ApexParser#enumConstantName.
    def enterEnumConstantName(self, ctx:ApexParser.EnumConstantNameContext):
        pass

    # Exit a parse tree produced by ApexParser#enumConstantName.
    def exitEnumConstantName(self, ctx:ApexParser.EnumConstantNameContext):
        pass


    # Enter a parse tree produced by ApexParser#typeType.
    def enterTypeType(self, ctx:ApexParser.TypeTypeContext):
        pass

    # Exit a parse tree produced by ApexParser#typeType.
    def exitTypeType(self, ctx:ApexParser.TypeTypeContext):
        pass


    # Enter a parse tree produced by ApexParser#classOrInterfaceType.
    def enterClassOrInterfaceType(self, ctx:ApexParser.ClassOrInterfaceTypeContext):
        pass

    # Exit a parse tree produced by ApexParser#classOrInterfaceType.
    def exitClassOrInterfaceType(self, ctx:ApexParser.ClassOrInterfaceTypeContext):
        pass


    # Enter a parse tree produced by ApexParser#primitiveType.
    def enterPrimitiveType(self, ctx:ApexParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by ApexParser#primitiveType.
    def exitPrimitiveType(self, ctx:ApexParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by ApexParser#typeArguments.
    def enterTypeArguments(self, ctx:ApexParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by ApexParser#typeArguments.
    def exitTypeArguments(self, ctx:ApexParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by ApexParser#typeArgument.
    def enterTypeArgument(self, ctx:ApexParser.TypeArgumentContext):
        pass

    # Exit a parse tree produced by ApexParser#typeArgument.
    def exitTypeArgument(self, ctx:ApexParser.TypeArgumentContext):
        pass


    # Enter a parse tree produced by ApexParser#qualifiedNameList.
    def enterQualifiedNameList(self, ctx:ApexParser.QualifiedNameListContext):
        pass

    # Exit a parse tree produced by ApexParser#qualifiedNameList.
    def exitQualifiedNameList(self, ctx:ApexParser.QualifiedNameListContext):
        pass


    # Enter a parse tree produced by ApexParser#formalParameters.
    def enterFormalParameters(self, ctx:ApexParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by ApexParser#formalParameters.
    def exitFormalParameters(self, ctx:ApexParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by ApexParser#formalParameterList.
    def enterFormalParameterList(self, ctx:ApexParser.FormalParameterListContext):
        pass

    # Exit a parse tree produced by ApexParser#formalParameterList.
    def exitFormalParameterList(self, ctx:ApexParser.FormalParameterListContext):
        pass


    # Enter a parse tree produced by ApexParser#formalParameter.
    def enterFormalParameter(self, ctx:ApexParser.FormalParameterContext):
        pass

    # Exit a parse tree produced by ApexParser#formalParameter.
    def exitFormalParameter(self, ctx:ApexParser.FormalParameterContext):
        pass


    # Enter a parse tree produced by ApexParser#lastFormalParameter.
    def enterLastFormalParameter(self, ctx:ApexParser.LastFormalParameterContext):
        pass

    # Exit a parse tree produced by ApexParser#lastFormalParameter.
    def exitLastFormalParameter(self, ctx:ApexParser.LastFormalParameterContext):
        pass


    # Enter a parse tree produced by ApexParser#methodBody.
    def enterMethodBody(self, ctx:ApexParser.MethodBodyContext):
        pass

    # Exit a parse tree produced by ApexParser#methodBody.
    def exitMethodBody(self, ctx:ApexParser.MethodBodyContext):
        pass


    # Enter a parse tree produced by ApexParser#constructorBody.
    def enterConstructorBody(self, ctx:ApexParser.ConstructorBodyContext):
        pass

    # Exit a parse tree produced by ApexParser#constructorBody.
    def exitConstructorBody(self, ctx:ApexParser.ConstructorBodyContext):
        pass


    # Enter a parse tree produced by ApexParser#qualifiedName.
    def enterQualifiedName(self, ctx:ApexParser.QualifiedNameContext):
        pass

    # Exit a parse tree produced by ApexParser#qualifiedName.
    def exitQualifiedName(self, ctx:ApexParser.QualifiedNameContext):
        pass


    # Enter a parse tree produced by ApexParser#literal.
    def enterLiteral(self, ctx:ApexParser.LiteralContext):
        pass

    # Exit a parse tree produced by ApexParser#literal.
    def exitLiteral(self, ctx:ApexParser.LiteralContext):
        pass


    # Enter a parse tree produced by ApexParser#annotation.
    def enterAnnotation(self, ctx:ApexParser.AnnotationContext):
        pass

    # Exit a parse tree produced by ApexParser#annotation.
    def exitAnnotation(self, ctx:ApexParser.AnnotationContext):
        pass


    # Enter a parse tree produced by ApexParser#annotationName.
    def enterAnnotationName(self, ctx:ApexParser.AnnotationNameContext):
        pass

    # Exit a parse tree produced by ApexParser#annotationName.
    def exitAnnotationName(self, ctx:ApexParser.AnnotationNameContext):
        pass


    # Enter a parse tree produced by ApexParser#elementValuePairs.
    def enterElementValuePairs(self, ctx:ApexParser.ElementValuePairsContext):
        pass

    # Exit a parse tree produced by ApexParser#elementValuePairs.
    def exitElementValuePairs(self, ctx:ApexParser.ElementValuePairsContext):
        pass


    # Enter a parse tree produced by ApexParser#elementValuePair.
    def enterElementValuePair(self, ctx:ApexParser.ElementValuePairContext):
        pass

    # Exit a parse tree produced by ApexParser#elementValuePair.
    def exitElementValuePair(self, ctx:ApexParser.ElementValuePairContext):
        pass


    # Enter a parse tree produced by ApexParser#elementValue.
    def enterElementValue(self, ctx:ApexParser.ElementValueContext):
        pass

    # Exit a parse tree produced by ApexParser#elementValue.
    def exitElementValue(self, ctx:ApexParser.ElementValueContext):
        pass


    # Enter a parse tree produced by ApexParser#elementValueArrayInitializer.
    def enterElementValueArrayInitializer(self, ctx:ApexParser.ElementValueArrayInitializerContext):
        pass

    # Exit a parse tree produced by ApexParser#elementValueArrayInitializer.
    def exitElementValueArrayInitializer(self, ctx:ApexParser.ElementValueArrayInitializerContext):
        pass


    # Enter a parse tree produced by ApexParser#annotationTypeDeclaration.
    def enterAnnotationTypeDeclaration(self, ctx:ApexParser.AnnotationTypeDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#annotationTypeDeclaration.
    def exitAnnotationTypeDeclaration(self, ctx:ApexParser.AnnotationTypeDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#annotationTypeBody.
    def enterAnnotationTypeBody(self, ctx:ApexParser.AnnotationTypeBodyContext):
        pass

    # Exit a parse tree produced by ApexParser#annotationTypeBody.
    def exitAnnotationTypeBody(self, ctx:ApexParser.AnnotationTypeBodyContext):
        pass


    # Enter a parse tree produced by ApexParser#annotationTypeElementDeclaration.
    def enterAnnotationTypeElementDeclaration(self, ctx:ApexParser.AnnotationTypeElementDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#annotationTypeElementDeclaration.
    def exitAnnotationTypeElementDeclaration(self, ctx:ApexParser.AnnotationTypeElementDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#annotationTypeElementRest.
    def enterAnnotationTypeElementRest(self, ctx:ApexParser.AnnotationTypeElementRestContext):
        pass

    # Exit a parse tree produced by ApexParser#annotationTypeElementRest.
    def exitAnnotationTypeElementRest(self, ctx:ApexParser.AnnotationTypeElementRestContext):
        pass


    # Enter a parse tree produced by ApexParser#annotationMethodOrConstantRest.
    def enterAnnotationMethodOrConstantRest(self, ctx:ApexParser.AnnotationMethodOrConstantRestContext):
        pass

    # Exit a parse tree produced by ApexParser#annotationMethodOrConstantRest.
    def exitAnnotationMethodOrConstantRest(self, ctx:ApexParser.AnnotationMethodOrConstantRestContext):
        pass


    # Enter a parse tree produced by ApexParser#annotationMethodRest.
    def enterAnnotationMethodRest(self, ctx:ApexParser.AnnotationMethodRestContext):
        pass

    # Exit a parse tree produced by ApexParser#annotationMethodRest.
    def exitAnnotationMethodRest(self, ctx:ApexParser.AnnotationMethodRestContext):
        pass


    # Enter a parse tree produced by ApexParser#annotationConstantRest.
    def enterAnnotationConstantRest(self, ctx:ApexParser.AnnotationConstantRestContext):
        pass

    # Exit a parse tree produced by ApexParser#annotationConstantRest.
    def exitAnnotationConstantRest(self, ctx:ApexParser.AnnotationConstantRestContext):
        pass


    # Enter a parse tree produced by ApexParser#defaultValue.
    def enterDefaultValue(self, ctx:ApexParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by ApexParser#defaultValue.
    def exitDefaultValue(self, ctx:ApexParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by ApexParser#block.
    def enterBlock(self, ctx:ApexParser.BlockContext):
        pass

    # Exit a parse tree produced by ApexParser#block.
    def exitBlock(self, ctx:ApexParser.BlockContext):
        pass


    # Enter a parse tree produced by ApexParser#blockStatement.
    def enterBlockStatement(self, ctx:ApexParser.BlockStatementContext):
        pass

    # Exit a parse tree produced by ApexParser#blockStatement.
    def exitBlockStatement(self, ctx:ApexParser.BlockStatementContext):
        pass


    # Enter a parse tree produced by ApexParser#localVariableDeclarationStatement.
    def enterLocalVariableDeclarationStatement(self, ctx:ApexParser.LocalVariableDeclarationStatementContext):
        pass

    # Exit a parse tree produced by ApexParser#localVariableDeclarationStatement.
    def exitLocalVariableDeclarationStatement(self, ctx:ApexParser.LocalVariableDeclarationStatementContext):
        pass


    # Enter a parse tree produced by ApexParser#localVariableDeclaration.
    def enterLocalVariableDeclaration(self, ctx:ApexParser.LocalVariableDeclarationContext):
        pass

    # Exit a parse tree produced by ApexParser#localVariableDeclaration.
    def exitLocalVariableDeclaration(self, ctx:ApexParser.LocalVariableDeclarationContext):
        pass


    # Enter a parse tree produced by ApexParser#statement.
    def enterStatement(self, ctx:ApexParser.StatementContext):
        pass

    # Exit a parse tree produced by ApexParser#statement.
    def exitStatement(self, ctx:ApexParser.StatementContext):
        pass


    # Enter a parse tree produced by ApexParser#propertyBlock.
    def enterPropertyBlock(self, ctx:ApexParser.PropertyBlockContext):
        pass

    # Exit a parse tree produced by ApexParser#propertyBlock.
    def exitPropertyBlock(self, ctx:ApexParser.PropertyBlockContext):
        pass


    # Enter a parse tree produced by ApexParser#getter.
    def enterGetter(self, ctx:ApexParser.GetterContext):
        pass

    # Exit a parse tree produced by ApexParser#getter.
    def exitGetter(self, ctx:ApexParser.GetterContext):
        pass


    # Enter a parse tree produced by ApexParser#setter.
    def enterSetter(self, ctx:ApexParser.SetterContext):
        pass

    # Exit a parse tree produced by ApexParser#setter.
    def exitSetter(self, ctx:ApexParser.SetterContext):
        pass


    # Enter a parse tree produced by ApexParser#catchClause.
    def enterCatchClause(self, ctx:ApexParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by ApexParser#catchClause.
    def exitCatchClause(self, ctx:ApexParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by ApexParser#catchType.
    def enterCatchType(self, ctx:ApexParser.CatchTypeContext):
        pass

    # Exit a parse tree produced by ApexParser#catchType.
    def exitCatchType(self, ctx:ApexParser.CatchTypeContext):
        pass


    # Enter a parse tree produced by ApexParser#finallyBlock.
    def enterFinallyBlock(self, ctx:ApexParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by ApexParser#finallyBlock.
    def exitFinallyBlock(self, ctx:ApexParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by ApexParser#resourceSpecification.
    def enterResourceSpecification(self, ctx:ApexParser.ResourceSpecificationContext):
        pass

    # Exit a parse tree produced by ApexParser#resourceSpecification.
    def exitResourceSpecification(self, ctx:ApexParser.ResourceSpecificationContext):
        pass


    # Enter a parse tree produced by ApexParser#resources.
    def enterResources(self, ctx:ApexParser.ResourcesContext):
        pass

    # Exit a parse tree produced by ApexParser#resources.
    def exitResources(self, ctx:ApexParser.ResourcesContext):
        pass


    # Enter a parse tree produced by ApexParser#resource.
    def enterResource(self, ctx:ApexParser.ResourceContext):
        pass

    # Exit a parse tree produced by ApexParser#resource.
    def exitResource(self, ctx:ApexParser.ResourceContext):
        pass


    # Enter a parse tree produced by ApexParser#forControl.
    def enterForControl(self, ctx:ApexParser.ForControlContext):
        pass

    # Exit a parse tree produced by ApexParser#forControl.
    def exitForControl(self, ctx:ApexParser.ForControlContext):
        pass


    # Enter a parse tree produced by ApexParser#forInit.
    def enterForInit(self, ctx:ApexParser.ForInitContext):
        pass

    # Exit a parse tree produced by ApexParser#forInit.
    def exitForInit(self, ctx:ApexParser.ForInitContext):
        pass


    # Enter a parse tree produced by ApexParser#enhancedForControl.
    def enterEnhancedForControl(self, ctx:ApexParser.EnhancedForControlContext):
        pass

    # Exit a parse tree produced by ApexParser#enhancedForControl.
    def exitEnhancedForControl(self, ctx:ApexParser.EnhancedForControlContext):
        pass


    # Enter a parse tree produced by ApexParser#forUpdate.
    def enterForUpdate(self, ctx:ApexParser.ForUpdateContext):
        pass

    # Exit a parse tree produced by ApexParser#forUpdate.
    def exitForUpdate(self, ctx:ApexParser.ForUpdateContext):
        pass


    # Enter a parse tree produced by ApexParser#parExpression.
    def enterParExpression(self, ctx:ApexParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by ApexParser#parExpression.
    def exitParExpression(self, ctx:ApexParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by ApexParser#expressionList.
    def enterExpressionList(self, ctx:ApexParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by ApexParser#expressionList.
    def exitExpressionList(self, ctx:ApexParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by ApexParser#statementExpression.
    def enterStatementExpression(self, ctx:ApexParser.StatementExpressionContext):
        pass

    # Exit a parse tree produced by ApexParser#statementExpression.
    def exitStatementExpression(self, ctx:ApexParser.StatementExpressionContext):
        pass


    # Enter a parse tree produced by ApexParser#constantExpression.
    def enterConstantExpression(self, ctx:ApexParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by ApexParser#constantExpression.
    def exitConstantExpression(self, ctx:ApexParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by ApexParser#apexDbUpsertExpression.
    def enterApexDbUpsertExpression(self, ctx:ApexParser.ApexDbUpsertExpressionContext):
        pass

    # Exit a parse tree produced by ApexParser#apexDbUpsertExpression.
    def exitApexDbUpsertExpression(self, ctx:ApexParser.ApexDbUpsertExpressionContext):
        pass


    # Enter a parse tree produced by ApexParser#apexDbExpression.
    def enterApexDbExpression(self, ctx:ApexParser.ApexDbExpressionContext):
        pass

    # Exit a parse tree produced by ApexParser#apexDbExpression.
    def exitApexDbExpression(self, ctx:ApexParser.ApexDbExpressionContext):
        pass


    # Enter a parse tree produced by ApexParser#expression.
    def enterExpression(self, ctx:ApexParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ApexParser#expression.
    def exitExpression(self, ctx:ApexParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ApexParser#primary.
    def enterPrimary(self, ctx:ApexParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ApexParser#primary.
    def exitPrimary(self, ctx:ApexParser.PrimaryContext):
        pass


    # Enter a parse tree produced by ApexParser#creator.
    def enterCreator(self, ctx:ApexParser.CreatorContext):
        pass

    # Exit a parse tree produced by ApexParser#creator.
    def exitCreator(self, ctx:ApexParser.CreatorContext):
        pass


    # Enter a parse tree produced by ApexParser#createdName.
    def enterCreatedName(self, ctx:ApexParser.CreatedNameContext):
        pass

    # Exit a parse tree produced by ApexParser#createdName.
    def exitCreatedName(self, ctx:ApexParser.CreatedNameContext):
        pass


    # Enter a parse tree produced by ApexParser#innerCreator.
    def enterInnerCreator(self, ctx:ApexParser.InnerCreatorContext):
        pass

    # Exit a parse tree produced by ApexParser#innerCreator.
    def exitInnerCreator(self, ctx:ApexParser.InnerCreatorContext):
        pass


    # Enter a parse tree produced by ApexParser#arrayCreatorRest.
    def enterArrayCreatorRest(self, ctx:ApexParser.ArrayCreatorRestContext):
        pass

    # Exit a parse tree produced by ApexParser#arrayCreatorRest.
    def exitArrayCreatorRest(self, ctx:ApexParser.ArrayCreatorRestContext):
        pass


    # Enter a parse tree produced by ApexParser#mapCreatorRest.
    def enterMapCreatorRest(self, ctx:ApexParser.MapCreatorRestContext):
        pass

    # Exit a parse tree produced by ApexParser#mapCreatorRest.
    def exitMapCreatorRest(self, ctx:ApexParser.MapCreatorRestContext):
        pass


    # Enter a parse tree produced by ApexParser#setCreatorRest.
    def enterSetCreatorRest(self, ctx:ApexParser.SetCreatorRestContext):
        pass

    # Exit a parse tree produced by ApexParser#setCreatorRest.
    def exitSetCreatorRest(self, ctx:ApexParser.SetCreatorRestContext):
        pass


    # Enter a parse tree produced by ApexParser#classCreatorRest.
    def enterClassCreatorRest(self, ctx:ApexParser.ClassCreatorRestContext):
        pass

    # Exit a parse tree produced by ApexParser#classCreatorRest.
    def exitClassCreatorRest(self, ctx:ApexParser.ClassCreatorRestContext):
        pass


    # Enter a parse tree produced by ApexParser#explicitGenericInvocation.
    def enterExplicitGenericInvocation(self, ctx:ApexParser.ExplicitGenericInvocationContext):
        pass

    # Exit a parse tree produced by ApexParser#explicitGenericInvocation.
    def exitExplicitGenericInvocation(self, ctx:ApexParser.ExplicitGenericInvocationContext):
        pass


    # Enter a parse tree produced by ApexParser#nonWildcardTypeArguments.
    def enterNonWildcardTypeArguments(self, ctx:ApexParser.NonWildcardTypeArgumentsContext):
        pass

    # Exit a parse tree produced by ApexParser#nonWildcardTypeArguments.
    def exitNonWildcardTypeArguments(self, ctx:ApexParser.NonWildcardTypeArgumentsContext):
        pass


    # Enter a parse tree produced by ApexParser#typeArgumentsOrDiamond.
    def enterTypeArgumentsOrDiamond(self, ctx:ApexParser.TypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by ApexParser#typeArgumentsOrDiamond.
    def exitTypeArgumentsOrDiamond(self, ctx:ApexParser.TypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by ApexParser#nonWildcardTypeArgumentsOrDiamond.
    def enterNonWildcardTypeArgumentsOrDiamond(self, ctx:ApexParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass

    # Exit a parse tree produced by ApexParser#nonWildcardTypeArgumentsOrDiamond.
    def exitNonWildcardTypeArgumentsOrDiamond(self, ctx:ApexParser.NonWildcardTypeArgumentsOrDiamondContext):
        pass


    # Enter a parse tree produced by ApexParser#superSuffix.
    def enterSuperSuffix(self, ctx:ApexParser.SuperSuffixContext):
        pass

    # Exit a parse tree produced by ApexParser#superSuffix.
    def exitSuperSuffix(self, ctx:ApexParser.SuperSuffixContext):
        pass


    # Enter a parse tree produced by ApexParser#explicitGenericInvocationSuffix.
    def enterExplicitGenericInvocationSuffix(self, ctx:ApexParser.ExplicitGenericInvocationSuffixContext):
        pass

    # Exit a parse tree produced by ApexParser#explicitGenericInvocationSuffix.
    def exitExplicitGenericInvocationSuffix(self, ctx:ApexParser.ExplicitGenericInvocationSuffixContext):
        pass


    # Enter a parse tree produced by ApexParser#arguments.
    def enterArguments(self, ctx:ApexParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by ApexParser#arguments.
    def exitArguments(self, ctx:ApexParser.ArgumentsContext):
        pass



del ApexParser